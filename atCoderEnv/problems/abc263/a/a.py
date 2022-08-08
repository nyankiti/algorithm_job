from sys import stdin, exit


def main():
    A, B, C, D, E = map(int, stdin.readline().split())
    di = {}
    di[A] = di.get(A, 0) + 1
    di[B] = di.get(B, 0) + 1
    di[C] = di.get(C, 0) + 1
    di[D] = di.get(D, 0) + 1
    di[E] = di.get(E, 0) + 1

    keys = list(di.keys())
    if len(keys) == 2:
        if (di[keys[0]] == 2 and di[keys[1]] == 3) or (di[keys[0]] == 3 and di[keys[1]] == 2):
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
