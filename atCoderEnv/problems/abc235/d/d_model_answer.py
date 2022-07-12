from collections import deque


def main():
    a, N = map(int, input().split())
    M = 1
    while M <= N:
        M *= 10

    # M以下の数までしか探索する必要がない
    distances = [-1] * M
    Q = deque()
    distances[1] = 0

    Q.append(1)
    while len(Q):
        c = Q.popleft()
        c_dist = distances[c]
        op1 = a * c
        if op1 < M and distances[op1] == -1:
            distances[op1] = c_dist + 1
            Q.append(op1)

        if c >= 10 and c % 10 != 0:
            s = str(c)
            op2 = int(s[-1] + s[:-1])
            if op2 < M and distances[op2] == -1:
                distances[op2] = c_dist + 1
                Q.append(op2)

    print(distances[N])


if __name__ == '__main__':
    main()
