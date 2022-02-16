from platform import node
from sys import stdin


class Node(object):
    def __init__(self, value: int, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value: int, parent=-1) -> None:
        if self.root is None:
            self.root = Node(value, parent)
            return

        def _insert(node: Node, value: int, parent: Node) -> Node:
            if node is None:
                return Node(value, parent)

            if value < node.value:
                node.left = _insert(node.left, value, node)
            else:
                node.right = _insert(node.right, value, node)
            return node

        _insert(self.root, value, -1)

    def find(self, target):
        def _find(node: Node, target):
            if node is None:
                return False

            if target == node.value:
                return node
            elif target < node.value:
                return _find(node.left, target)
            else:
                return _find(node.right, target)

        return _find(self.root, target)

    def min_value(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def max_value(self, node: Node) -> Node:
        current = node
        while current.right is not None:
            current = current.right
        return current

    def remove(self, target):
        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return node

            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # 以下の二つは同じ結果になる(right側の一番小さいnodeを持ってくるか、left側の一番大きいnodeを持ってくるかは好み)
                # どちらを使い分けるかは問題の指示による

                # ①right側の一番小さいnodeを持ってくるversion
                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)

                # ②left側の一番大きいnodeを持ってくるversion
                # temp = self.max_value(node.left)
                # node.value = temp.value
                # node.left = _remove(node.left, temp.value)

            return node
        _remove(self.root, target)

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
    elif query[0] == "find":
        find_res = binary_tree.find(int(query[1]))
        if find_res:
            print("yes")
        else:
            print("no")
    elif query[0] == "delete":
        binary_tree.delete(int(query[1]))
    elif query[0] == "print":
        binary_tree.inorderTreeWalk()
        print()
        binary_tree.preorderTreeWalk()
        print()
