'''
fibonacci数列に再帰関数を使うのが必ずしも正しいとは限らない。
詳しくは以下の記事を参照
https://qiita.com/cohey0727/items/117b55cf73c7784359c0
'''

from sys import stdin

n = int(stdin.readline())


memo = {}


def fib(n):
    if memo.get(n):
        return memo[n]

    if n <= 1:
        return 1

    ans = fib(n-1) + fib(n-2)
    memo[n] = ans
    return ans


# iterativeに記述した方法
def fibonacci(n):
    fk, fk_1 = 1, 1
    for _ in range(n):
        fk, fk_1 = fk_1, fk + fk_1
    return fk


print(fib(n))
print(fibonacci(n))
