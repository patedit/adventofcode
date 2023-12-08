from advent import Advent

advent = Advent(2021, 22)

class Inst():
    def __init__(self, params):
        self.power = params[0] == 'on'
        coors = params[1].split(",")
        self.x_orig, self.x_dest = [int(i) for i in coors[0][2:].split("..")]
        self.y_orig, self.y_dest = [int(i) for i in coors[1][2:].split("..")]
        self.z_orig, self.z_dest = [int(i) for i in coors[2][2:].split("..")]

    def is_on(self):
        return self.power

def _update_cubes(inst, cubes):
    for x in range(inst.x_orig, inst.x_dest + 1):
        for y in range(inst.y_orig, inst.y_dest+1):
            for z in range(inst.z_orig, inst.z_dest+1):
                if inst.is_on():
                    cubes.add((x,y,z))
                elif (x,y,z) in cubes:
                    cubes.remove((x,y,z))
def part1():
    cubes = set()
    limit = 50
    for line in advent.lines:
        inst = Inst(line.split(" "))
        if abs(inst.x_orig) > limit or abs(inst.y_orig) > limit or abs(inst.z_orig) > limit: continue
        _update_cubes(inst, cubes)
    return len(cubes)

print(part1())