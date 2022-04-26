from sys import stdin


def main():
    A, B, C, D, E, F, X = map(int, stdin.readline().split())
    t_distance = 0
    t_time = 0
    is_rest = False
    duration = 0
    while t_time < X:
        if is_rest:
            duration += 1
            t_time += 1
            if duration == C:
                is_rest = False
                duration = 0
        else:
            duration += 1
            t_time += 1
            t_distance += B
            if duration == A:
                is_rest = True
                duration = 0

    a_distance = 0
    a_time = 0
    is_rest = False
    duration = 0
    while a_time < X:
        if is_rest:
            duration += 1
            a_time += 1
            if duration == F:
                is_rest = False
                duration = 0
        else:
            duration += 1
            a_time += 1
            a_distance += E
            if duration == D:
                is_rest = True
                duration = 0

    if t_distance > a_distance:
        print("Takahashi")
    elif t_distance == a_distance:
        print("Draw")
    else:
        print("Aoki")


if __name__ == '__main__':
    main()
