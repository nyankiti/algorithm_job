from sys import stdin
from collections import deque

"""
ボールを一つずつ扱っていては、間に合わないし、メモリも足りない・
そこで、(ボールに書いてある数字, ボールの個数) のリストをdequeに入れて、塊ごとまとめて処理します。 
このアルゴリズムをランレングス圧縮といいます。
（ランレングスとは、Run Lengthのことです。そのままですね。日本語では連長圧縮といいます）
"""


def main():
    Q = int(stdin.readline())
    dq = deque()
    flg = True
    for _ in range(Q):
        *query, = stdin.readline().split()

        if query[0] == "1":
            li = [int(query[1]), int(query[2])]  # ボールに書いてある数字, ボールの個数
            dq.append(li)
        elif query[0] == "2":
            temp_sum = 0
            to_take_num = int(query[1])
            while to_take_num > 0:
                left_elem = dq[0]
                if to_take_num >= left_elem[1]:
                    to_take_num -= left_elem[1]
                    temp_sum += left_elem[0]*left_elem[1]
                    dq.popleft()
                else:
                    temp_sum += left_elem[0]*to_take_num
                    dq[0] = [left_elem[0], left_elem[1] - to_take_num]
                    to_take_num = 0

            print(temp_sum)

            flg = False

    if flg:
        print()


if __name__ == '__main__':
    main()
