from sys import stdin

"""
しゃくとり法を用いて計算量を O(n) に改善した実装
"""

def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    *X, = map(int, stdin.readline().split())
    
    # leftを動かすタイプのしゃくとり虫
    def solve(x):
        count = 0
        right = 0
        sum = 0
        for left in range(N):
            # sum に A[right] を加えても大丈夫なら right を動かす */
            while right < N and sum + A[right] <= x:
                sum += A[right]
                right += 1

            # break した状態で right は条件を満たす最大
            count += (right - left)

            # left をインクリメントする準備
            if (right == left) :
                #right が left に重なったら right も動かす
                right += 1 
            else: 
                #left のみがインクリメントされるので sum から a[left] を引く
                sum -= A[left]
        return count


    # rightを動かすタイプのしゃくとり虫
    def solve(x):
        count = 0
        cumulative_sum = 0
        left = 0
        for right in range(N + 1):
            while cumulative_sum > x:
                cumulative_sum -= A[left]
                left += 1
            count += right - left

            if right < N:
                cumulative_sum += A[right]
        return count

        
    for x in X:
        print(solve(x))





if __name__ == '__main__':
    main()