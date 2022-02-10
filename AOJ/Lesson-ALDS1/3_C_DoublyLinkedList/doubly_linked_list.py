
class Node(object):
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data) -> None:
        new_node = Node(data)
        # 最初の一つ目のデータ
        if self.head is None:
            self.head = new_node
            return

        # データを追加する場所へ移動
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def delete(self, data) -> None:
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

        current_node = self.head
        while current_node and current_node.data != data:
            current_node = current_node.next

        # 指定されたデータが存在しなかったとき
        if current_node == None:
            return

        # 指定されたデータが最後だったとき
        if current_node.next == None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None


d = DoublyLinkedList()
d.append(5)
d.append(2)
d.append(9)
d.append(4)
