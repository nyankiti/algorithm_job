import collections
import math
from typing import Optional


class Node:
    def __init__(self, frequency, char, left=None, right=None) -> None:
        self.char = char
        self.frequency = 0
        self.parent = None
        self.left = left
        self.right = right

    def register_parent(self, parent):
        self.parent = parent


S = input()

# counterは辞書型をベースにしている
counter = collections.Counter(S)


current_min_frequency_node: Optional[Node] = None

for index, value in enumerate(reversed(counter.most_common())):
    char, count = value
    # print("%s : %d" % (char, count))
    node = Node(char, count)

    if index != 0:
        if current_min_frequency_node.count < node.count:
            parent_node = Node(
                "", count + current_min_frequency_node.count, current_min_frequency_node, node)
        else:
            parent_node = Node(
                "", count + current_min_frequency_node.count, node, current_min_frequency_node)
        current_min_frequency_node.register_parent(parent_node)
        node.register_parent(parent_node)

    else:
        # 最初の一回目は二つ以上のnodeがないので親を作れない
        current_min_frequency_node = node
