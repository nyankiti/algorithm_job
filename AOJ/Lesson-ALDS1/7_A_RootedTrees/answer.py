# 参考：https://tech-shelf.hatenablog.com/entry/algorithm/tree
from sys import stdin


class Node(object):
    def __init__(self):
        self.children = []
        self.parent = -1
        self.type = None
        self.depth = None


n = int(stdin.readline())
tree = [Node() for _ in range(n)]


for _ in range(n):
    *node_info, = map(int, stdin.readline().split())
    node_id = node_info[0]
    node_rank = node_info[1]
    if node_rank > 0:
        tree[node_id].children = node_info[2:]
        tree[node_id].type = "internal node"
    else:
        tree[node_id].type = "leaf"

    # childにparent情報の反映
    for child in tree[node_id].children:
        tree[child].parent = node_id


# 上でtreeを作成した時点で、parentが-1のものがtoorだとわかる
root_id = 0
for node_id, node in enumerate(tree):
    if node.parent == -1:
        root_id = node_id
tree[root_id].type = "root"


# 各nodeのdepthの算出
def calc_depth(node_id, depth=0):
    tree[node_id].depth = depth
    for child in tree[node_id].children:
        calc_depth(child, depth+1)


calc_depth(root_id, 0)

# 出力
for node_id, node in enumerate(tree):
    print("node {}: parent = {}, depth = {}, {}, {}".format(
        node_id, node.parent, node.depth, node.type, node.children))
