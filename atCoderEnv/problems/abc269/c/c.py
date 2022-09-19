from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    N_bin = str(bin(N)[2:])
    # print(N_bin)
    # bit全探索
    one_count = N_bin.count("1")
    # print(one_count)

    one_positions = []
    for index, bit in enumerate(N_bin):
        if bit == "1":
            one_positions.append(index)
    one_positions.reverse()

    for i in range(2**one_count):
        temp = ["0"]*len(N_bin)
        k = 0
        for j in range(one_count):
            if ((i >> j) & 1):
                temp[one_positions[k]] = "1"
            k += 1

        ans = int("".join(temp), 2)
        print(ans)


if __name__ == '__main__':
    main()
