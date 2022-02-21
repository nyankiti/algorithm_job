'''
最長共通部分列とは列X、Yが与えられた時に共通する部分列の数である。
共通文字列の順番は同じでなければいけないが、文字列が連続している必要はない。
以下のサイトが最もLongest Common Subsequenceの理解に役立った
https://qiita.com/_rdtr/items/c49aa20f8d48fbea8bd2

pythonの実装時に参考にしたサイト
https://qiita.com/ophhdn/items/dce35806b2458d59e086

二つのタンパク質のアミノ酸配列の類似度を検討する際に、最長共通部分列はひとつの指標となる
'''
from sys import stdin


def get_longest_common_subsequence(X, Y):
    # DPの要素DP[i][j]は、Xを左からi文字文切り出した部分文字列と
    # Yを左からj文字文切り出した部分文字列の共通部分列長である。
    dp = [[0]*(len(X)+1) for _ in range(len(Y) + 1)]

    for i in range(len(Y)):
        for j in range(len(X)):
            if Y[i] == X[j]:
                # dpデーブルは0番目の共通部分列長を0として格納する必要があるので、一つインクリメントしたindexに保存する
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    # debug用
    for row in dp:
        print(*row)

    return dp[-1][-1]


n = int(stdin.readline())
for i in range(n):
    X = input()
    Y = input()
    print(X)
    print(Y)
    print(get_longest_common_subsequence(X, Y))
