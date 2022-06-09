from sys import stdin
import bisect


MOD = 10**9 + 7


def main():
    N = int(stdin.readline())
    S = input()

    counter = {
        "a": [],
        "t": [],
        "c": [],
        "o": [],
        "d": [],
        "e": [],
        "r": []
    }

    for i, chr in enumerate(S):
        if chr in "atcoder":
            counter[chr].append(i)

    ans = 0

    for li in counter.values():
        print(li)

    for r_num in reversed(counter["r"]):
        prev_num = r_num
        sub_ans = 1

        e_index = bisect.bisect_left(counter["e"], prev_num)
        sub_ans = sub_ans * len(counter["e"][:e_index]) % MOD
        if len(counter["e"]) == e_index:
            e_index -= 1
        prev_num = counter["e"][e_index]

        d_index = bisect.bisect_left(counter["d"], prev_num)
        sub_ans = sub_ans * len(counter["d"][:d_index]) % MOD
        if len(counter["d"]) == d_index:
            d_index -= 1
        prev_num = counter["d"][d_index]

        o_index = bisect.bisect_left(counter["o"], prev_num)
        sub_ans = sub_ans * len(counter["o"][:o_index]) % MOD
        if len(counter["o"]) == o_index:
            o_index -= 1
        prev_num = counter["o"][o_index]

        c_index = bisect.bisect_left(counter["c"], prev_num)
        sub_ans = sub_ans * len(counter["c"][:c_index]) % MOD
        if len(counter["c"]) == c_index:
            c_index -= 1
        prev_num = counter["c"][c_index]

        t_index = bisect.bisect_left(counter["t"], prev_num)
        sub_ans = sub_ans * len(counter["t"][:t_index]) % MOD
        if len(counter["t"]) == t_index:
            t_index -= 1
        prev_num = counter["t"][t_index]

        a_index = bisect.bisect_left(counter["a"], prev_num)
        sub_ans = sub_ans * len(counter["a"][:a_index]) % MOD
        if len(counter["a"]) == a_index:
            a_index -= 1
        prev_num = counter["a"][a_index]

        ans += sub_ans
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
