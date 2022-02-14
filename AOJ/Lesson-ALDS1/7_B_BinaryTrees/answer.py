from sys import stdin


class Node(object):
    def __init__(self):
        self.children = []
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
            tree[node_id].children = [children[1]]
        elif children[1] == -1:
            tree[children[0]].sibling = -1
            tree[children[0]].parent = node_id
            tree[node_id].children = [children[0]]
        else:
            # siblingの登録
            tree[children[0]].sibling, tree[children[1]
                                            ].sibling = children[1], children[0]
            #　parentの登録
            tree[children[0]].parent, tree[children[1]].parent = node_id, node_id
            # childrenの登録
            tree[node_id].children = children


# 上でtreeを作成した時点で、parentが-1のものがtoorだとわかる
root_id = 0
for node_id, node in enumerate(tree):
    if node.parent == -1:
        root_id = node_id
tree[root_id].type = "root"
tree[root_id].sibling = -1


# 各nodeのdepthの算出
def calc_depth(node_id, depth=0):
    tree[node_id].depth = depth
    if len(tree[node_id].children) != 0:
        for child in tree[node_id].children:
            calc_depth(child, depth+1)


calc_depth(root_id, 0)


# heightの算出
def maxHeight(root: Node):
    if len(root.children) == 0:
        return 0
    elif len(root.children) == 1:
        return 1 + maxHeight(tree[root.children[0]])
    else:
        return 1 + max(maxHeight(tree[root.children[0]]), maxHeight(tree[root.children[1]]))


for node_id, node in enumerate(tree):
    if node.type == "leaf":
        node.height = 0
    else:
        node.height = maxHeight(node)


# 出力
for node_id, node in enumerate(tree):
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(
        node_id, node.parent, node.sibling, len(node.children), node.depth, node.height, node.type))
