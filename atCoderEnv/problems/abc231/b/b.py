from sys import stdin


def main():
    N = int(stdin.readline())
    counter = {}
    for _ in range(N):
        S = input()
        counter[S] = counter.get(S, 0) + 1
    max_val = max(counter.values())
    for key, value in counter.items():
        if value == max_val:
            print(key)
            break


if __name__ == '__main__':
    main()
