from collections import deque


def main():
    N = int(input())
    S = input()
    ans = deque((N,))
    print(list(ans))
    for i in reversed(range(N)):
        if S[i] == "L":
            ans.append(i)
        else:
            ans.appendleft(i)
    print(*ans)


main()