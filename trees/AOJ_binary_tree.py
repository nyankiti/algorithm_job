# AOJ Lesson-ALDS1の "7_B_BinaryTree" と "7_C_TreeWalk" で実装したbinary treeのメソッドををクラスメソッドとして書き直す

class Node(object):
    def __init__(self):
        self.children = []
        self.parent = -1
        self.sibling = None
        self.depth = None
        self.height = None
        self.type = None


class BinarySearchTree(object):

    def __init__(self) -> None:
        self.root = None
