from random import randint

class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        self.vis = False

    def add_node(self, n):
        if n.val < self.val:
            if self.left is None:
                self.left = n
            else:
                self.left.add_node(n)
        else:
            if self.right is None:
                self.right = n
            else:
                self.right.add_node(n)

    def in_order(self):
        nodes = []
        res = []
        nodes.append(self)
        while nodes:
            curr = nodes[-1]
            if curr.left is not None and not curr.left.vis:
                nodes.append(curr.left)
            else:
                res.append(curr.val)
                curr.vis = True
                nodes.pop()
                if curr.right is not None and not curr.right.vis:
                    nodes.append(curr.right)
        return res


root = Node(25)
for _ in range(20):
    root.add_node(Node(randint(1, 50)))
res = root.in_order()
print(*res)
