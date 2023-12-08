from advent import Advent
import copy

advent = Advent(2021, 18)

class Snailfish():
    left, right, parent, val = None, None, None, None

    def __init__(self, line=None):
        if line is None: return
        curr = self
        for c in line:
            if c == '[':
                curr.left = Snailfish()
                curr, curr.parent = curr.left, curr
            elif c == ',':
                curr.right = Snailfish()
                curr, curr.parent = curr.right, curr
            elif c == ']':
                curr = curr.parent
            else:
                curr.val, curr = c, curr.parent

    def reduce(self):
        while self.explode() or self.split(): continue

    def _should_split(self):
        if self.val and int(self.val) >= 10:
            return True
        l,r=False,False
        if self.left:
            l = self.left._should_split()
        if self.right:
            r = self.right._should_split()
        return l or r

    def _should_explode(self, lvl=0):
        if lvl == 4 and not self.val:
            return True
        l, r = False, False
        if self.left:
            l = self.left._should_explode(lvl+1)
        if self.right:
            r = self.right._should_explode(lvl+1)
        return l or r
    
    def _find_parent(self, left=True):
        prev_node = self
        curr_parent = self.parent
        while curr_parent and (curr_parent.left if left else curr_parent.right) == prev_node:
            prev_node = prev_node.parent
            curr_parent = curr_parent.parent
        return None if not curr_parent else (curr_parent.left if left else curr_parent.right)

    def _find_edge(self, left=True):
        curr_node = self
        while curr_node and not curr_node.val:
            curr_node = curr_node.right if left else curr_node.left
        return curr_node

    def explode(self, lvl=0):
        if lvl >= 4 and not self.val:
            closest_parent = self._find_parent(True)
            if closest_parent:
                edge_node = closest_parent._find_edge(True)
                edge_node.val = str(int(edge_node.val) + int(self.left.val))

            closest_parent = self._find_parent(False)
            if closest_parent:
                edge_node = closest_parent._find_edge(False)
                edge_node.val = str(int(edge_node.val) + int(self.right.val))

            self.left = False
            self.right = False
            self.val = '0'

            return True

        left_exploded, right_exploded = False, False
        if self.left:
            left_exploded = self.left.explode(lvl+1)
        if self.right:
            right_exploded = self.right.explode(lvl+1)

        return left_exploded or right_exploded
    
    def split(self):
        if self.val and int(self.val) >= 10:
            half_val = int(self.val) // 2
            self.left, self.right = Snailfish(), Snailfish()
            self.left.val = str(half_val)
            self.left.parent, self.right.parent = self, self
            self.right.val = str(half_val + int(self.val) % 2)
            self.val = None
            return self

        left_split, right_split = None, None

        if self.left:
            left_split = self.left.split()
        if not left_split and self.right:
            right_split = self.right.split()

        return left_split or right_split

    def magnitude(self):
        if self.val: return int(self.val)
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __str__(self):
        if self.val: return self.val
        return '[' + str(self.left) + ',' + str(self.right) + ']'
        
    def __add__(self, other):
        sum = Snailfish()
        sum.left, sum.right = copy.deepcopy(self), copy.deepcopy(other)
        sum.left.parent, sum.right.parent = sum, sum
        sum.reduce()
        return sum

# Part 1
sn = Snailfish(advent.lines[0])
for line in advent.lines[1:]:
    sn += Snailfish(line)
print(sn.magnitude())

# Part 2
snailfishes = [Snailfish(line) for line in advent.lines]
max_magnitude = 0
for i, sn_i in enumerate(snailfishes):
    for j, sn_j in enumerate(snailfishes):
        if i != j:
            max_magnitude = max(max_magnitude, (sn_i + sn_j).magnitude())
print(max_magnitude)