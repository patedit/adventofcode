from advent import Advent

advent = Advent(2022, 7, use_file=False, test="")

disk = {"/": {"is_dir": True, "size": 0}}
dirs_into, curr_dir = [], disk

def _update_size_parents(dirs_into, file_size):
    parent_dir = disk
    for dir in dirs_into:
        parent_dir = parent_dir[dir]
        parent_dir["size"] += file_size

for cmd in advent.lines:
    if cmd.startswith("$ ls"): continue
    if cmd.startswith("$ cd"):
        new_dir = cmd.split("$ cd ")[1]
        if new_dir == "..":
            dirs_into.pop()
            curr_dir = disk
            for subdir in dirs_into:
                curr_dir = curr_dir[subdir]
        else:
            dirs_into.append(new_dir)
            curr_dir = curr_dir[new_dir]
    elif cmd.startswith("dir"):
        dir_name = cmd.split("dir ")[1]
        curr_dir[dir_name] = {"is_dir": True, "size": 0}
    else:
        file_size, file_name = cmd.split(" ")
        file_size = int(file_size)
        curr_dir[file_name] = {"is_dir": False, "size": file_size}
        _update_size_parents(dirs_into, file_size)

total_size = 0
def part1_dfs(r):
    global total_size
    if r["is_dir"] == True and r["size"] <= 100000:
        total_size += r["size"]
    for dir in r:
        if dir == "size" or dir == "is_dir": continue
        part1_dfs(r[dir])

part1_dfs(disk["/"])

print(total_size)

min_bytes_to_delete = 30000000 - (70000000 - disk["/"]["size"])

solution = float('inf')
def part2_dfs(r):
    global solution
    if r["is_dir"] == True and r["size"] >= min_bytes_to_delete:
        solution = min(solution, r["size"])
    for dir in r:
        if dir == "size" or dir == "is_dir": continue
        part2_dfs(r[dir])
part2_dfs(disk["/"])
print(solution)