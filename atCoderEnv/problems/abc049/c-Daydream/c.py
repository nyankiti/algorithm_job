#!/usr/bin python
import sys

keywords = ["dream", "dreamer", "erase", "eraser"]
len_keywords = len(keywords)
'''
全探索する必要はない。
文字を取り出してkeywoedsに一致するかどうかを繰り返せば良いだけ！！

=> 前から探索すると、eraser と erase、dreamerとdreamが混同してしまうので、うまく探索できない。
=> 後ろから文字を切り出して探索すべき！！
'''

S = input()
T = ""

while True:
    flg = False
    for i in range(len_keywords):
        len_keyword = len(keywords[i])
        # 後ろからチェックしているので、スライスに注意
        if S[-len_keyword:] == keywords[i]:
            flg = True
            S = S[:-len_keyword]
            T = S[-len_keyword:] + T
            if len(S) == 0:
                print("YES")
                sys.exit()

    if flg == False:
        print("NO")
        sys.exit()


# 反則的な解答---------------------------------------------------------
# s = input().replace("eraser", "").replace(
#     "erase", "").replace("dreamer", "").replace("dream", "")
# print("YES" if len(s) == 0 else "NO")
# -------------------------------------------------------------------
