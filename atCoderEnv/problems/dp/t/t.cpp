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

int N;
string s;
ll dp[3009][3009], dp_sum[3009][3009];
int main() {
    cin >> N >> s;
    dp[0][0] = 1;
    for (int i = 1; i < N; i++) {
        // dp_sumの更新
        for (int j = 0; j <= i; j++) {
            dp_sum[i - 1][j] = dp[i - 1][j];
            if (j - 1 >= 0)
                dp_sum[i - 1][j] += dp_sum[i - 1][j - 1];
            dp_sum[i - 1][j] %= MOD;
        }
        for (int j = 0; j <= i; j++) {
            if (s[i - 1] == '<') {
                if (j - 1 >= 0)
                    dp[i][j] = dp_sum[i - 1][j - 1];
            } else {
                dp[i][j] = dp_sum[i - 1][i - 1];
                if (j - 1 >= 0)
                    dp[i][j] -= dp_sum[i - 1][j - 1];
                dp[i][j] %= MOD;
            }
        }
    }
    ll ans = 0;
    for (int i = 0; i < N; i++) {
        ans += dp[N - 1][i];
        ans %= MOD;
    }
    if (ans < 0)
        ans += MOD;
    cout << ans << endl;
    return 0;
}