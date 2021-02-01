# from __future__ import annotations
from typing import Optional, Any


class Node(object):
  def __init__(self, data: Any, next_node = None, prev_node = None):
    self.data = data
    self.next = next_node
    self.prev = prev_node



class DoublyLinkedList(object):

  def __init__(self, head = None) -> None:
    self.head = head

  def append(self, data: Any) -> None:
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    current_node = self.head
    
    while current_node.next:
      current_node = current_node.next

    current_node.next = new_node
    new_node.prev = current_node

  def insert(self, data: Any) -> None:
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    self.head.prev = new_node
    new_node.next = self.head
    self.head = new_node

  def print(self) -> None:
    current_node = self.head
    while current_node:
      print(current_node.data)
      current_node = current_node.next


  def remove(self, data: Any) -> None:
    current_node = self.head
    if current_node and current_node.data == data:
      if current_node.next is None:
        current_node = None
        self.head = None
        return
      else:
        next_node = current_node.next
        next_node.prev = None
        current_node = None
        self.head = next_node
        return
    
    while current_node and current_node.data != data:
      current_node = current_node.next

    if current_node is None:
      return 

    # 消去するノードが最後のノードだったとき
    if current_node.next is None:
      prev = current_node.prev
      prev.next = None
      current_node = None
      return

    else:
      next_node = current_node.next
      prev_node = current_node.prev
      next_node.prev = prev_node
      prev_node.next = next_node
      current_node = None 
      return 

  def reverse_iterative(self) -> None:
    prev_node = None
    current_node = self.head
    while current_node:
      prev_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = prev_node

      # リンクが逆になるので次のノードに進む時はprevで指定
      current_node = current_node.prev
    if prev_node:
      self.head = prev_node.prev

  def reverse_recursive(self) -> None:
    def reverse_recursive(current_node) -> Optional[None]:
      if not current_node:
        return None

      prev_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = prev_node
    
      if current_node.prev is None:
        return current_node

      return reverse_recursive(current_node.prev)

    self.head = reverse_recursive(self.head)



# -------------------------------------------------------
# 双方向リストのソート-----------------------------------
# -------------------------------------------------------


  def sort(self) -> None:
    if self.head is None:
      return

    current_node = self.head
    while current_node.next:

      next_node = current_node.next
      while next_node:
        if current_node.data > next_node.data:
          current_node.data , next_node.data = next_node.data, current_node.data
        next_node = next_node.next
      current_node = current_node.next










if __name__ == '__main__':
  d = DoublyLinkedList()
  d.append(5)
  d.append(2)
  d.append(9)
  d.append(4)
  d.print()
  print('##################')
  d.sort()
  d.print()


