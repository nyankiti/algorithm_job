from sys import stdin


class Node(object):
    def __init__(self):
        # self.children = []
        self.left_child = None
        self.right_child = None
        self.parent = -1
        self.sibling = None
        self.depth = None
        self.height = None
        self.type = None


n = int(stdin.readline())
# 配列の -1 は最後の要素を指すので、childrenが存在しない場合の-1と混同することに注意
tree = [Node() for _ in range(n)]


for _ in range(n):
    *node_info, = map(int, stdin.readline().split())
    node_id = node_info[0]

    children = node_info[1:]
    if children == [-1, -1]:
        tree[node_id].type = "leaf"
    else:
        tree[node_id].type = "internal node"
        if children[0] == -1:
            tree[children[1]].sibling = -1
            tree[children[1]].parent = node_id
            tree[node_id].right_child = children[1]
        elif children[1] == -1:
            tree[children[0]].sibling = -1
            tree[children[0]].parent = node_id
            tree[node_id].left_child = children[0]
        else:
            # siblingの登録
            tree[children[0]].sibling, tree[children[1]
                                            ].sibling = children[1], children[0]
            #　parentの登録
            tree[children[0]].parent, tree[children[1]].parent = node_id, node_id
            # childrenの登録
            tree[node_id].left_child = children[0]
            tree[node_id].right_child = children[1]


# 上でtreeを作成した時点で、parentが-1のものがtoorだとわかる
root_id = 0
for node_id, node in enumerate(tree):
    if node.parent == -1:
        root_id = node_id
tree[root_id].type = "root"
tree[root_id].sibling = -1


def preorder(root_id):
    if root_id is not None:
        node = tree[root_id]
        print("", root_id, end="")
        preorder(node.left_child)
        preorder(node.right_child)


print("Preorder")
preorder(root_id)


def inorder(root_id):
    if root_id is not None:
        node = tree[root_id]
        inorder(node.left_child)
        print("", root_id, end="")
        inorder(node.right_child)


print("\nInorder")
inorder(root_id)


def postorder(root_id: int):
    if root_id is not None:
        node = tree[root_id]
        postorder(node.left_child)
        postorder(node.right_child)
        print("", root_id, end="")


print("\nPostorder")
postorder(root_id)
print()
