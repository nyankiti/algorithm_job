'''

'''
import random

class Tree:
  def __init__(self, data, left= None, right=None):
    self.data = data
    self.left = left
    self.right = right


def reverseTree(tree):
  if tree is None:
    return
  tree.left, tree.right = tree.right, tree.left
  reverseTree(tree.reft)
  reverseTree(tree.right)


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main()
  print(s)