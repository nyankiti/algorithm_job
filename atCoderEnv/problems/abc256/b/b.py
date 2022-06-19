from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    current_state = [False, False, False, False]

    point = 0
    for a in A:
        current_state[0] = True
        for num in range(3, -1, -1):
            if current_state[num] == True:
                if num + a < 4:
                    current_state[num+a] = True
                    current_state[num] = False
                elif num + a >= 4:
                    point += 1
                    current_state[num] = False

    print(point)


if __name__ == '__main__':
    main()
