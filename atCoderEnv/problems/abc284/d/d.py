from sys import stdin, setrecursionlimit
import math

setrecursionlimit(10**6)


def main():
    T = int(stdin.readline())
    for _ in range(T):
        N = int(stdin.readline())
        # Nの大きさによって、後ろから探索する場合も考える
        for p in range(2, math.ceil(N**(1/3))+1):
            if N % p == 0:
                A = N//p
                if A % p == 0:
                    q = N//(p*p)
                    print(p, q)
                    break
                else:
                    q = p
                    p = int((N/q)**0.5)
                    print(p, q)
                    break
            # q = N / (p*p)
            # if q.is_integer():
            #     q = int(q)
            #     if p*p*q == N:
            #         print(p, q)
            #         break
            # # pとqが逆の可能性
            # q = p
            # p = math.sqrt(N/q)
            # if p.is_integer():
            #     p = int(p)
            #     if p*p*q == N:
            #         print(p, q)
            #         break


if __name__ == '__main__':
    main()
