from sys import stdin

"""
左を固定して、条件を満たすまで探索する 計算量 O(n^2) の実装
"""
def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    *X, = map(int, stdin.readline().split())
    
    
    def solve(x):
        count = 0
        for l in range(N):
            temp_sum = 0
            for r in range(l, N):
                if temp_sum + A[r] <= x:
                    temp_sum += A[r]
                    count += 1
                else:
                    break
        return count

        
    for x in X:
        print(solve(x))





if __name__ == '__main__':
    main()