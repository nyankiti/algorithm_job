from sys import stdin


def main():
    N, X = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    A.sort()

    # if X in A:
    #     print("Yes")
    # else:
    #     print("No")

    def binary_search(x):
        left, right = 0, N-1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] == x:
                return True
            elif A[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return False

    print("Yes" if binary_search(X) else "No")


if __name__ == '__main__':
    main()
