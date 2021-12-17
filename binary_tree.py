# binary 0と1という意味
# データをbinary構造で保存しておくと検索するときも整列するときも消去する時も単純なリスト構造より計算量（ifによる半定回数）を格段に減らすことができる

# まず、それぞれのノードのクラス設計を作る
# ノードには自身が持つ値、右の行き先のノード、左の行き先のノード、という3つの情報が格納される
class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def min_value(node: Node, value: int) -> Node:
  current = node
  while current.left is not None:
    current = current.left
  return current

def remove(node: Node, value: int) -> Node:
  if node is None:
    return node
  
  # 消したいノードの値が今見ているノードの値より小さい時
  if value < node.value:
    node.left = remove(node.left, value)
  # 消したいノードの値が今見ているノードの値より大きい時
  elif value > node.value:
    node.right = remove(node.right, value)
  # 消したい値と今見ているノードの値が一致すれば消す処理に入る
  else:
    if node.left is None:
      return node.right
    elif node.right is None:
      return node.left

      temp = min_value(node.right)
      node.value = temp.value
      node.right = remove(node.right, temp.value)
  return node







# 並び替えシリーズ---------------------------------------------------------------------

# 再帰をうまく用いて整列させる
# 再帰を一つ抜け出すと上に戻るので左の奥まで進んだとしても、戻りながら整列してくれる
# left root rightの順で見る
def inorder(node: Node) -> None:
  if node is not None:
    # 左にノードがあるかぎり再帰し続ける
    inorder(node.left)
    print(node.value)
    inorder(node.right)

# inorderの逆向きverのreverse_order
def reverse_order(node: Node) -> None:
  if node is not None:
    reverse_order(node.right)
    print(node.value)
    reverse_order(node.left)

# root left right の順でみるpreorder
def preorder(node: Node) -> None:
  if node is not None:
    print(node.value)
    preorder(node.left)
    preorder(node.right)

# --------------------------------------------------------------
# サーチ--------------------------------------------------------

def  search(node: Node, value: int) -> bool:
  if node is None:
    return False

  #rootの値と探す値が一致した時 
  if node.value == value:
    return True
  elif node.value > value:
    return search(node.left, value)
  elif node.value < value:
    return search(node.right, value)







if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    # print(root.right.right.value)
    inorder(root)
    print("------------------------------")
    reverse_order(root)
    print("------------------------------")
    preorder(root)
    print('searchメソッドのテスト')
    print(search(root, 11))
    print(search(root, 10))

    remove(root, 7)
    print('after remove 7----------------')
    inorder(root)