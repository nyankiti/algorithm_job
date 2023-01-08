from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    def binary_search(li, X):
        left_index = 0
        right_index = len(li)-1
        while left_index <= right_index:
            middle_index = (left_index+right_index)//2
            if A[middle_index] == X:
                return middle_index
            elif A[middle_index] < X:
                left_index = middle_index+1
            else:
                right_index = middle_index-1
        return middle_index

    print(binary_search(A, X)+1)


if __name__ == '__main__':
    main()
