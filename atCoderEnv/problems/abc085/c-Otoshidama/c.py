#!/usr/bin python

N, SUM = map(int, input().split(" "))

flg = False

for x in range(N+1):
    for y in range(N+1):
        if 9000*x + 4000*y == SUM - 1000*N:
            z = (SUM - 10000*x - 5000*y) // 1000
            if z >= 0 and x + y + z == N:
                # print(str(x) + " " + str(y) + " " + str(z))
                # printメソッドは可変長の引数を受け取って空白で区切ってprintしてくれる
                print(x, y, z)
                flg = True
                break
    else:
        # 内側のfor文が全て回った場合のみelseに入って以下のcontinueが実行される。
        continue
    # 内側のfor文がbreakによって中断された場合、以下のbreakが実行される
    break


if flg == False:
    print("-1 -1 -1")
