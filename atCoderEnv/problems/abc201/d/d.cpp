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

int H, W;
int A[2009][2009];
/*
dp[i][j] => (i, j) からスタートした時、(自分-相手) の最大値
=> 右下からdpを埋めていく必要がある

メモ化再帰関数での実装
*/
int memo[2009][2009];
int rec(int i, int j) {
    if (i == H && j == W)
        return 0;
    if (memo[i][j] != INF)
        return memo[i][j];

    int res = -INF;
    if (j + 1 <= W) {
        res = max(res, A[i][j + 1] - rec(i, j + 1));
    }
    if (i + 1 <= H) {
        res = max(res, A[i + 1][j] - rec(i + 1, j));
    }
    memo[i][j] = res;
    return res;
}

int main() {
    cin >> H >> W;
    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            char val;
            cin >> val;
            A[i][j] = val == '+' ? 1 : -1;
            memo[i][j] = INF;
        }
    }
    int score = rec(1, 1);
    if (score == 0)
        cout << "Draw" << endl;
    else if (score < 0)
        cout << "Aoki" << endl;
    else
        cout << "Takahashi" << endl;
    return 0;
}