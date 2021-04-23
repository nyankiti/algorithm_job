'''
dfs : depth first search
'''
import random


# define binary tree
# class Node(object):
#     def __init__(self, value: int):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinarySearchTree(object):
#   def __init__(self):
#     self.root = None
  
#   def insert(self, value):
#     if self.root is None:
#       self.root = Node(value)
      

#     def _insert(node, value):
#       if node is None:
#         return Node(value)

#       if value < node.value:
#         node.left = _insert(node.left, value)
#       else:
#         node.right = _insert(node.right, value)
#       return node
    
#     _insert(self.root, value)



class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self) -> None:
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

    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)


    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False

            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)

    def min_value(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, value: int) -> None:
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

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        _remove(self.root, value)

    def dfsPreorder(self)->None:
        def _dfsPreorder(root)->None:
          if root is None:
            return
          print(root.value)
          _dfsPreorder(root.left)
          _dfsPreorder(root.right)

        _dfsPreorder(self.root)

    def dfsPostorder(self)->None:
        def _dfsPostorder(root)->None:
          if root is None:
            return
          _dfsPostorder(root.left)
          _dfsPostorder(root.right)
          print(root.value)

        _dfsPostorder(self.root)

    def dfsInorder(self)->None:
        def _dfsInorder(root)->None:
          if root is None:
            return
          _dfsInorder(root.left)
          print(root.value)
          _dfsInorder(root.right)

        _dfsInorder(self.root)




    # def dfsInorder(root):
    #   if root is None:
    #     return
    #   dfsInorder(root.left)
    #   print(root.value)
    #   dfsInorder(root.right)

    # def dfsPostorder(root):
    #   if root is None:
    #     return
    #   dfsPostorder(root.left)
    #   dfsPostorder(root.right)
    #   print(root.value)



#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  binary_tree = BinarySearchTree()
  binary_tree.insert(1)
  binary_tree.insert(2)
  binary_tree.insert(3)
  binary_tree.insert(4)
  binary_tree.insert(5)
  binary_tree.insert(6)

  # binary_tree.dfsPreorder()
  # binary_tree.dfsPostorder()
  binary_tree.dfsInorder()