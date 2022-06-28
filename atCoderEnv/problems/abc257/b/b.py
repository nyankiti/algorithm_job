from sys import stdin


def main():
    N, K, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    *L, = map(int, stdin.readline().split())

    mas = [False]*(N+1)
    for a in A:
        mas[a] = True

    for l in L:
        count = 0
        target_index = -1
        for index, val in enumerate(mas):
            if val:
                count += 1
                if count == l:
                    target_index = index
                    break

        if target_index == N:
            continue
        if mas[target_index+1] == False:
            mas[target_index+1] = True
            mas[target_index] = False

        # print(mas)

    ans = []
    for i, val in enumerate(mas):
        if val:
            ans.append(i)

    print(*ans)


if __name__ == '__main__':
    main()
