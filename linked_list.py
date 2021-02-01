# linked_listとは配列など、インデックス番号のあるデータ群の管理方法である



# annotationをimportするとクラスメソッドの定義時の引数にそのクラスオブジェクトを入れることを、タイプ指定で書ける
# from __future__ import annotations
from typing import Any

# まず、データと次のノードオブジェクトを持つノードのクラスを作る
# nextには次のノードオブジェクトを指定する
class Node(object):
  # 第３引数のNodeはこのクラスオブジェクトということ,デフォルトはNoneで指定しないならばリンクの最終到着点がNoneということになる
    def __init__(self, data: Any, next_node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):
  # まずリンクの最初であるheadを作る。headには最初のノードオブジェクトを格納する
  # デフォルトはNoneであり、リンクにデータが入っていないことを示す
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
      # まず、新しいデータを格納したノードオブジェクトを作る
        new_node = Node(data)
        # まだデータが入っていなければheadに新しく追加するノードオブジェクトをリンクさせる
        if self.head is None:
            self.head = new_node
            return

        # データを加える最後のNodeをwhile文を用いて最初のheadから登っていく
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # 最後のノードの後ろに新しいノードをリンクする
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        # ノードの最初に入れたいときは、既存のheadを新しいノードのポインターにして、新たなheadに加えたノードのデータをリンクする
        new_node = Node(data)
        # headはデータを持っていないので、headが指すノードオブジェクトを入れ替えてあげるだけで良い
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        current_node = self.head
        # current_nodeの存在をif current_nodeで確かめている
        # 最初のデータと削除したいデータが一致した場合
        if current_node and current_node.data == data:
          # 消すcurrent_nodeのリンクを先のノードのリンクに変更してから消す
            self.head = current_node.next
            current_node = None
            return

        # 削除したいノードが途中にある場合while文で探す
        # 削除したいノードの一つ前のノードと一つ次のノードをつなげるため、一つ前のノードを保存しておく
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        # 削除するデータがない場合(最後のデータのnextはNoneを指す)
        if current_node is None:
            return

        # 削除したいノードの一つ前のノードと一つ次のノードをつなげる
        previous_node.next = current_node.next
        current_node = None


    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            # current_nodeと一つ手前のprevious_nodeをリンクさせる（逆方向に進む準備）
            current_node.next = previous_node
            # データも一つ手前のノードに移る
            previous_node = current_node

            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self) -> None:
        # インナー関数には名前の最初に _ をつける
        def _reverse_recursive(current_node, previous_node):
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)

    def reverse_even(self) -> None:
        def _reverse_even(head: Node, previous_node: Node):
            if head is None:
                return None

            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
                return head

        self.head = _reverse_even(self.head, None)




    def reverse_even(self) -> None:
        def _reverse_even(head: Node, previous_node: Node) -> Optional[Nonde]:
            if head is None:
                return None

            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
                return head

        self.head = _reverse_even(self.head, None)










if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.print()
    print('--------------')
    l.reverse_iterative()
    l.print()
    print('---------------')
    l.reverse_recursive()
    l.print()