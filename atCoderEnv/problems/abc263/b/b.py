from sys import stdin


class People:
    def __init__(self) -> None:
        self.parent = None


def main():
    N = int(stdin.readline())
    *P, = map(int, stdin.readline().split())

    peoples = [People() for _ in range(N)]
    # print(peoples)

    for i, p in enumerate(P):
        target = peoples[i+1]
        target.parent = p

    # for val in peoples:
    #     print(val.parent)

    count = 1
    current = peoples[N-1]
    while current.parent != 1:
        count += 1
        current = peoples[current.parent-1]
    print(count)


if __name__ == '__main__':
    main()
