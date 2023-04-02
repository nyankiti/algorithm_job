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

// Sのi番目までにおいて、chokudaiのj番目までを作ることができる数
int dp[10][100009];
int main() {
    string S, chokudai = "chokudai";
    cin >> S;
    int n = S.size();
    for (int i = 0; i < n; i++) {
        dp[0][i] = 1;
    }
    for (int i = 1; i <= chokudai.size(); i++) {
        for (int j = 1; j <= n; j++) {
            if (chokudai[i - 1] == S[j - 1]) {
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD;
            } else {
                dp[i][j] = dp[i][j - 1];
            }
        }
    }
    cout << dp[chokudai.size()][n] << endl;

    return 0;
}