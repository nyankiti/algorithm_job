#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>; // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1 << 30) - 1)
#define LINF (1LL << 60)
// 非常に小さい値を表す epsilon。浮動小数展比較において、誤差の範囲を表すために使用する。10^(-10)を表している。
#define EPS (1e-10)

string K;
ll D;
ll dp[100009][109][2];
/* 桁DP
  dp[i][j][c] = 上から i 桁目までの 桁和%D が j であり、c = 今まで決めた部分が K と一致しているかどうか
*/
int main() {
    cin >> K >> D;
    int N = K.size();
    dp[0][0][1] = 1;
    for (int i = 1; i <= N; i++) {
        for (int j = 0; j < D; j++) {
            int digit = K[i - 1] - '0';
            for (int k = 0; k < 10; k++) {
                dp[i][j][0] += dp[i - 1][((j - k) % D + D) % D][0];
                if (k < digit)
                    dp[i][j][0] += dp[i - 1][((j - k) % D + D) % D][1];
                dp[i][j][0] %= MOD;
            }
            dp[i][j][1] = dp[i - 1][((j - digit) % D + D) % D][1];
        }
    }
    cout << (dp[N][0][0] + dp[N][0][1] + MOD - 1) % MOD << endl;
    return 0;
}