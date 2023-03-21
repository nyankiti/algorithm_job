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

int H, W, A[19][19], dp[19][19];
int ans = 0;
unordered_set<int> visited;
// visitedで管理しながらDFSする

void dfs(int i, int j) {
    if (i == H && j == W) {
        ans += 1;
        return;
    }

    if (i < H) {
        if (visited.count(A[i + 1][j]) == 0) {
            visited.insert(A[i + 1][j]);
            dfs(i + 1, j);
            visited.erase(A[i + 1][j]);
        }
    }
    if (j < W) {
        if (visited.count(A[i][j + 1]) == 0) {
            visited.insert(A[i][j + 1]);
            dfs(i, j + 1);
            visited.erase(A[i][j + 1]);
        }
    }
}
int main() {
    cin >> H >> W;
    for (int i = 1; i <= H; i++)
        for (int j = 1; j <= W; j++)
            cin >> A[i][j];

    visited.insert(A[1][1]);
    dfs(1, 1);
    cout << ans << endl;

    return 0;
}