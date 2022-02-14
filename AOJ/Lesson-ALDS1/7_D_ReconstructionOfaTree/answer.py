'''
方針
1. ある部分木について、preorderから、節点を見つける

2. 見つけた節点でinorderを分割し、左部分木、右部分木を作る（実際はinorderの列）

3. 2で作った左右それぞれの部分木に対応するpreorderの列を生成する。

4. 2,3で作った左右それぞれのpreorderとinorderの列に対して、1を再帰的に実行する
'''
from sys import stdin
from typing import List


class Node(object):
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.parent = -1


n = int(stdin.readline())
*preorder, = map(int, stdin.readline().split())
*inorder, = map(int, stdin.readline().split())

tree = [Node() for _ in range(n+1)]


def reconstruction(inorder: List[int], preorder: List[int], parent=-1):
    if len(preorder) == 0:
        return None
    # ある部分木について、preorderから、節点を見つける
    root = preorder[0]
    current_node = tree[root]
    # nodeのparentの登録
    current_node.parent = parent

    if len(preorder) == 1:
        return root

    root_index_in_inorder = inorder.index(root)
    # 見つけた節点でinorderを分割し、左部分木、右部分木を作る
    left_inorder = inorder[:root_index_in_inorder]
    right_inorder = inorder[root_index_in_inorder+1:]

    # 上で作った左右それぞれの部分木に対応するpreorderの列を生成する。
    left_preorder = [
        i for i in preorder if i in left_inorder]
    right_preorder = [
        i for i in preorder if i in right_inorder]

    # 作った左右それぞれのpreorderとinorderの列に対して、1を再帰的に実行する
    current_node.left_child = reconstruction(
        left_inorder, left_preorder, root)
    current_node.right_child = reconstruction(
        right_inorder, right_preorder, root)

    # rootを返す(この値が呼び出し元のnodeのchildとなる)
    return root


root_id = preorder[0]
reconstruction(inorder, preorder)

# 出力部分
result = []


def postorderWalk(root_id: int):
    if root_id is not None:
        node = tree[root_id]
        postorderWalk(node.left_child)
        postorderWalk(node.right_child)
        result.append(root_id)


postorderWalk(root_id)
print(*result)
