from advent import Advent
from collections import defaultdict, deque

advent = Advent(2023, 25, use_file=False)

'''
Creates a graph with edges.
Go through all the edges and count the number of times each edge is used.
The edges that are used the most are the ones that are most likely to be. Suprisingly, it works.

Later I found max-flow min-cut algorithm, which is probably what I should have used (networkx has it, but feels like cheating)
'''

wires = defaultdict(list)
connections = defaultdict(int)
for line in advent.lines:
    component, other_components = line.split(': ')
    for other_component in other_components.split():
        wires[component].append(other_component)
        wires[other_component].append(component)
        connection = tuple([component, other_component])
        connections[''.join(sorted(connection))] = 0


for node in wires:
    visited = set([node])
    q = deque([(node, None)])

    while q:
        node, from_node = q.popleft()
        if from_node:
            connections[''.join(sorted(tuple([node, from_node])))] += 1
        for neighbor in wires[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append([neighbor, node])

# TODO Improve. Test input has the same value for the top 3 edges. It was index 0, 2 and 4.
# Puzzle input does not give the same number of edges on top 3 so it works for that input
max_connections = sorted(connections, key=lambda x: connections[x], reverse=True)[:3]

for c in max_connections:
    node1, node2 = c[:3], c[3:]
    wires[node1].remove(node2)
    wires[node2].remove(node1)

visited = set([node]) # any node should be fine
q = [node]
while q:
    curr = q.pop()
    for neighbor in wires[curr]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)

comp1_size = len(wires) - len(visited)
comp2_size = len(visited)

print(comp1_size, comp2_size, comp1_size * comp2_size)
