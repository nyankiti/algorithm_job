from sys import stdin


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def main():
    N, A, B = map(int, stdin.readline().split())
    all_sum = N*(1+N)//2
    GCD = gcd(A, B)
    LMC = A * B // GCD
    if A != B:
        # AとBが互いに素の時
        # Aの倍数の項数
        N_A = N//A
        A_sum = N_A * (2*A+(N_A-1)*A) // 2

        # Bの倍数の項数
        N_B = N//B
        B_sum = N_B * (2*B+(N_B-1)*B) // 2

        # AとBの最小公倍数の倍数の項数
        N_LMC = N//LMC
        LMC_sum = N_LMC * (2*LMC + (N_LMC - 1)*LMC) // 2

        print(all_sum - A_sum - B_sum + LMC_sum)
    else:
        N_A = N//A
        A_sum = N_A * (2*A+(N_A-1)*A) // 2
        print(all_sum - A_sum)


if __name__ == '__main__':
    main()
