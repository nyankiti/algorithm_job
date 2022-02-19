from sys import stdin, maxsize

# ここで実装する完全二分木は親子、兄弟間で値の制約が制約が一切無い。
# ただ、新しくpushされる要素を順番に木に引っ付けるだけ


class CompleteBinaryTree(object):
    def __init__(self) -> None:
        self.heap = [-1 * maxsize]
        self.current_size = 0

    def parent_index(self, index: int):
        if index == 0:
            return False
        return index // 2

    def left_child_index(self, index: int):
        if 2 * index <= self.current_size:
            return 2 * index
        else:
            return False

    def right_child_index(self, index: int):
        if 2 * index + 1 <= self.current_size:
            return 2 * index + 1
        else:
            return False

    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1


H = int(stdin.readline())
*numbers, = map(int, stdin.readline().split())

tree = CompleteBinaryTree()

for num in numbers:
    tree.push(num)


for index, value in enumerate(numbers):
    print("node {}: key = {}, ".format(index+1, value), end="")
    if tree.parent_index(index+1):
        parent_key = tree.heap[tree.parent_index(index+1)]
        print("parent key = {}, ".format(parent_key), end="")
    if tree.left_child_index(index+1):
        left_child_key = tree.heap[tree.left_child_index(index+1)]
        print("left key = {}, ".format(left_child_key), end="")
    if tree.right_child_index(index+1):
        right_child_key = tree.heap[tree.right_child_index(index+1)]
        print("right key = {}, ".format(right_child_key), end="")
    print()
