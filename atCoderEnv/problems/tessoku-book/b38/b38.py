from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S = input()
    heights = [1]*(N)

    for i, char in enumerate(S):
        if char == "A":
            heights[i+1] = heights[i]+1
        else:
            heights[i+1] = heights[i]-1

    min_height = min(heights)
    if min_height < 1:
        diff = 1 - min_height
        for i in range(N):
            heights[i] += diff
    print(heights)
    # 条件を満たした最小値を更新する
    if S[0] == "A":
        heights[0] = 1
    elif S[0] == "B":
        heights[0] = heights[1]+1

    for i in range(1, N-1):
        if S[i-1] == "A" and S[i] == "A":
            heights[i] = heights[i-1]+1
        elif S[i-1] == "B" and S[i] == "A":
            heights[i] = 1
        elif S[i-1] == "A" and S[i] == "B":
            heights[i] = heights[i-1] + 1
        elif S[i-1] == "B" and S[i] == "B":
            heights[i] = heights[i+1] + 1

    # if S[N-2] == "A":
    #     heights[N-1] = heights[N-2]+1
    # else:
    #     heights[N-1] = 1
    print(heights)
    print(sum(heights))


if __name__ == '__main__':
    main()
