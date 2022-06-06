from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *a, = map(int, stdin.readline().split())

    # i + nK で 交換可能
    for i in range(min(K, N, abs(N-K))):
        temp_li = []
        j = i
        while j < N:
            temp_li.append(a[j])
            j += K
        temp_li.sort()

        j = i
        temp_index = 0
        while j < N:
            a[j] = temp_li[temp_index]
            temp_index += 1
            j += K

    for i in range(N-1):
        if a[i] > a[i+1]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    main()
