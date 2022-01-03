'''
dfs : depth first search
'''
import random


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node, value):
            if node is None:
                return Node(value)

            if node.value < value:
                node.right = _insert(node.right, value)
            else:
                node.left = _insert(node.left, value)
            return node

        _insert(self.root, value)

    def dfsPreorder(self):
        def _dfsPreorder(root):
            if root is None:
                return
            print(root.value)
            _dfsPreorder(root.left)
            _dfsPreorder(root.right)

        _dfsPreorder(self.root)

    def dfsInorder(self):
        def _dfsInorder(root):
            if root is None:
                return
            _dfsInorder(root.left)
            print(root.value)
            _dfsInorder(root.right)

        _dfsInorder(self.root)

    def dfsPostorder(self):
        def _dfsPostorder(root):
            if root is None:
                return
            _dfsPostorder(root.left)
            _dfsPostorder(root.right)
            print(root.value)
        _dfsPostorder(self.root)


if __name__ == '__main__':
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(44)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    print("inorder--------------------------------------")
    tree.dfsInorder()
    print("postorder------------------------------------")
    tree.dfsPostorder()
    print("preorder-------------------------------------")
    tree.dfsPreorder()
