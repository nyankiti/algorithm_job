class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)
    if node.value < value:
        node.right = insert(node.right, value)
    else:
        node.left = insert(node.left, value)

    return node

