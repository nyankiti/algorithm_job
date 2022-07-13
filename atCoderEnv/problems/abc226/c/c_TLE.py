from collections import deque
from sys import stdin


def main():
    N = int(stdin.readline())
    skills_A = []
    skills_T = []

    for i in range(N):
        T, K, *A, = map(int, stdin.readline().split())
        skills_A.append(A)
        skills_T.append(T)

    must_skills = {}
    visited = [N-1]
    dq = deque()
    for a in skills_A[N-1]:
        must_skills[a-1] = True
        dq.append(a-1)

    while dq:
        poped = dq.pop()
        for a in skills_A[poped]:
            must_skills[a-1] = True
            if a-1 not in visited:
                dq.append(a-1)

    ans = 0
    for val in must_skills.keys():
        ans += skills_T[val-1]
    ans += skills_T[-1]

    print(ans)


if __name__ == '__main__':
    main()
