from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    *numbers,  = map(int, list(input()))
    len_numbers = len(numbers)

    ans = 0
    for i in range(2**len_numbers):
        left = []
        right = []
        for j in range(len_numbers):
            if ((i >> j) & 1):
                left.append(numbers[j])
            else:
                right.append(numbers[j])

        if len(left) > 0 and len(right) > 0:
            left.sort(reverse=True)
            right.sort(reverse=True)
            left_num = int("".join(map(str, left)))
            right_num = int("".join(map(str, right)))

            ans = max(left_num*right_num, ans)

    print(ans)


if __name__ == '__main__':
    main()
