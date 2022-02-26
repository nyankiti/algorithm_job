from sys import stdin

H, W = map(int, stdin.readline().split())

# 入力の受け取り-----------------------------------------------
target = []

for _ in range(H):
    target.append(input())

# for row in target:
#     print(row)


R, C = map(int, stdin.readline().split())

pattern = []

for _ in range(R):
    pattern.append(input())

# for row in pattern:
#     print(row)
# 探索の開始---------------------------------------------------

if -R+1 == 0:
    search_target = target[:]
else:
    search_target = target[:-R+1]

for index, row in enumerate(search_target):
    for j in range(W-C+1):
        # 最初の1行がマッチしているかのチェック
        if pattern[0] == row[j: j+C]:
            # 続くパターンのチェック
            k = 1
            flg = True
            while k < R:
                if pattern[k] != target[index+k][j: j+C]:
                    flg = False
                    break
                k += 1
            else:
                pass

            if flg:
                print(index, j)


# LTE,,,,,全探索ではなく、別の探索方法がある気がすす
