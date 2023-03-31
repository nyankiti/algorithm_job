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

int n, a[20][20];
ll dp[1 << 16], cost[1 << 16];
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    for (int s = 0; s < (1 << n); s++) {
        for (int i = 0; i < n; i++) {
            if ((s >> i) % 2 == 0)
                continue;
            for (int j = i + 1; j < n; j++) {
                if ((s >> j) % 2 == 0)
                    continue;
                cost[s] += a[i][j];
            }
        }
    }

    dp[0] = 0;
    for (int s = 1; s < (1 << n); s++) {
        for (int t = s; t > 0; t = (t - 1) & s) {
            dp[s] = max(dp[s], dp[s - t] + cost[t]);
        }
    }
    cout << dp[(1 << n) - 1] << endl;
    return 0;
}