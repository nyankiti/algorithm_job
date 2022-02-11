import sys
# n = int(input())
n = int(sys.stdin.readline())
DICT = {}

# for i in range(n):
for s in sys.stdin:
    print(s)
    # query = input().split()
    query = s.split()
    # query = sys.stdin.readline().split()
    if query[0] == "insert":
        DICT[query[1]] = True
    if query[0] == "find":
        if query[1] in DICT:
            print("yes")
        else:
            print("no")


# input() を使うと4.8sかかった
# stdin を使うと 1.16〜1.4sかかった。
# => stdinの方が圧倒的に早い！
