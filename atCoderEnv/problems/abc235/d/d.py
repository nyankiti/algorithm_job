from sys import stdin


# この解き方ではafter_contestのtest caseが通らない、、、、

def main():
    a, N = map(int, stdin.readline().split())

    def inverse_rotate(x):
        x_str = str(x)
        return int(x_str[1:] + x_str[0])

    count = 0
    ans_li = []
    visited = []

    def check_visited(rotated_target, count):
        for index, val in enumerate(visited):
            if val[0] == rotated_target:
                if val[1] < count:
                    visited[index] = (-1, -1)
                    return True
                else:
                    return False
        return True

    def serch(target, count):
        visited.append((target, count))

        if target == 1:
            ans_li.append(count)

        if target % a == 0:
            serch(target//a, count+1)

        rotated_target = inverse_rotate(target)
        if check_visited(rotated_target, count):
            serch(rotated_target, count+1)

    serch(N, count)
    print(ans_li)

    if len(ans_li) == 0:
        print(-1)
    else:
        print(min(ans_li))


if __name__ == '__main__':
    main()
