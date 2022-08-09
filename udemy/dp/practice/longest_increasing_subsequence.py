from sys import stdin


def main():

    # tabulation
    def lis(arr):
        dp = [0] * len(arr)
        dp[0] = 1

        for i, el in enumerate(arr):
            maxlen = 0
            # 以前の
            for j in range(i):
                if arr[j] < el:
                    maxlen = max(maxlen, dp[j])
            dp[i] = maxlen + 1

        print(dp)
        return max(dp)

    ans = lis([7, 5, 2, 4, 7, 2, 3, 6, 4, 5, 12, 1, 7])
    print(ans)

    # memorization vol1
    def lis_rec(arr):
        len_arr = len(arr)

        def rec(i):
            maxlen = 0
            for j in range(i + 1, len_arr):
                if arr[j] > arr[i]:
                    maxlen = max(maxlen, rec(j))
            return 1 + maxlen

        ans = 0
        for i in range(len_arr):
            ans = max(ans, rec(i))
        return ans

    ans = lis_rec([7, 5, 2, 4, 7, 2, 3, 6, 4, 5, 12, 1, 7])
    print(ans)

    # memorization vol2
    def lis_rec_2(arr):
        lookup = {}

        def rec_2(pos, prev):
            if (pos, prev) in lookup:
                return lookup[(pos, prev)]

            if pos == len(arr):
                return 0
            elif arr[pos] <= prev:
                lookup[(pos, prev)] = rec_2(pos + 1, prev)
            else:
                lookup[(pos, prev)] = max(1 + rec_2(pos + 1, arr[pos]),
                                          rec_2(pos + 1, prev))
            return lookup[(pos, prev)]

        return rec_2(0, float("-inf"))

    ans = lis_rec_2([7, 5, 2, 4, 7, 2, 3, 6, 4, 5, 12, 1, 7])
    print(ans)


if __name__ == '__main__':
    main()