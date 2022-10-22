from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    tree = [Node(i) for i in range(2*N+1)]
    rank = [0]*(2*N+1)

    # for i, a in enumerate(A):
    #     node = tree[a-1]
    #     node.left = tree[2*i]
    #     node.right = tree[2*i+1]
    #     rank[2*i] = rank[a-1]+1
    #     rank[2*i+1] = rank[a-1]+1

    for i in range(1, N+1):
        a = A[i-1]
        rank[2*i-1] = rank[a-1]+1
        rank[2*i] = rank[a-1]+1
    for val in rank:
        print(val)


if __name__ == '__main__':
    main()
