from sys import stdin, setrecursionlimit, exit

setrecursionlimit(10**6)


def main():
    S = input()
    len_S = len(S)
    T = input()
    len_T = len(T)

    # 最初の x = 0の時は全探索する
    S_prime = S[:0] + S[len_S-(len_T-0):]
    # 最初の S_prime と Tの距離を diff_dist 記録しておく
    diff_dist = 0
    is_first_example_matched = True
    for i in range(len_T):
        if S_prime[i] == "?" or T[i] == "?":
            continue
        if S_prime[i] != T[i]:
            diff_dist += 1
            is_first_example_matched = False

    print("Yes" if is_first_example_matched else "No")
    # print(diff_dist)
    # print("first S prime", S_prime)

    for x in range(1, len_T+1):
        S_prime = S[:x] + S[len_S-(len_T-x):]
        # 各ループで、新しく入る文字と、抜ける文字に注目する
        new_in = S[x-1]
        new_in_pos = x-1
        last_out = S[len_S-(len_T-x)-1]
        # print(x, S_prime)
        # print("new in", new_in, "last out", last_out)
        # print("new in pos", new_in_pos)
        if (T[new_in_pos] != "?"):
            if (T[new_in_pos] != last_out and (T[new_in_pos] == new_in or new_in == "?")):
                diff_dist -= 1
            elif (T[new_in_pos] == last_out and (T[new_in_pos] == new_in or new_in == "?")):
                pass
            else:
                diff_dist += 1

        if diff_dist <= 0:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
