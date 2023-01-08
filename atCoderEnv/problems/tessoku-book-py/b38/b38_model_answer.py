from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S = input()
    A_heights = [1]*(N)
    B_heights = [1]*(N)

    for i, char in enumerate(S):
        if char == "A":
            A_heights[i+1] = A_heights[i]+1

    for i in range(N-2, -1, -1):
        if S[i] == "B":
            B_heights[i] = B_heights[i+1]+1

    ans = []
    for a, b in zip(A_heights, B_heights):
        ans.append(max(a, b))

    # print(A_heights)
    # print(B_heights)
    # print(ans)
    print(sum(ans))


if __name__ == '__main__':
    main()
