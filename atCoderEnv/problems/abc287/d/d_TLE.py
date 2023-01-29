from sys import stdin, setrecursionlimit, exit

setrecursionlimit(10**6)


def main():
    S = input()
    len_S = len(S)
    T = input()
    len_T = len(T)

    for x in range(len_T+1):
        S_prime = S[:x] + S[len_S-(len_T-x):]
        # print(x, S_prime)
        # S_primeとTのマッチを考える
        for i in range(len_T):
            if S_prime[i] == "?" or T[i] == "?":
                continue
            if S_prime[i] != T[i]:
                print("No")
                break
        else:
            print("Yes")


if __name__ == '__main__':
    main()
