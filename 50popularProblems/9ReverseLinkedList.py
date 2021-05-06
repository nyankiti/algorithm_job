'''

'''
import random

def main():
  class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

def reverse_iterative(li):
  previous_node = None
  current_node = li.head
  while current_node is not None:
    next_node = current_node.next
    current_node.next = previous_node

    previous_node = current_node
    current_node = next_node
  li.head = previous_node

def reverse_recursive_by_inside(li):
  def _reverse_recursive(node):
    if node is None or node.next is None:
      return node
    reversed = _reverse_recursive(node.next)
    node.next.next = node
    node.next = None
    return reversed
  li.head = _reverse_recursive(li.head)

def reverse_recursive_by_sakai(self):
  def _reverse_recursive(current_node, previous_node):
    if not current_node:
      return previous_node

    next_node = current_node.next
    current_node.next = previous_node

    previous_node = current_node
    current_node = next_node
    return _reverse_recursive(current_node, previous_node)

  li.head = _reverse_recursive(self.head, None)




#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main()
  print(s)