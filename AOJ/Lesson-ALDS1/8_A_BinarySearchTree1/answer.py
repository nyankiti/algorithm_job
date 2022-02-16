from sys import stdin


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)

    def inorderTreeWalk(self):

        def _inorderTreeWalk(node: Node):
            if node is not None:
                _inorderTreeWalk(node.left)
                print("", node.value, end="")
                _inorderTreeWalk(node.right)

        _inorderTreeWalk(self.root)

    def preorderTreeWalk(self):

        def _preorderTreeWalk(node: Node):
            if node is not None:
                print("", node.value, end="")
                _preorderTreeWalk(node.left)
                _preorderTreeWalk(node.right)

        _preorderTreeWalk(self.root)


n = int(stdin.readline())
binary_tree = BinarySearchTree()

for i in range(n):
    *query, = stdin.readline().split()
    if query[0] == "insert":
        binary_tree.insert(int(query[1]))
    elif query[0] == "print":
        binary_tree.inorderTreeWalk()
        print()
        binary_tree.preorderTreeWalk()
        print()
