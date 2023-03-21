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

/*
頂点 1 の根とした根付き木を考える。それ以下、部分木をdpできる

dp[v][c]: 頂点 v を根とする部分木を塗る時、頂点vをc色に塗る場合の数
dp[v][白] = Π(dp[u][白] + dp[u][黒]) (白同士は隣合っても良い)
v の子 u に対して総積をとる

dp[v][黒] = Π(dp[u][白])
v の子 u に対して総積をとる

※
0 => 白
1 => 黒

上のようなDPをDFSで埋めていくと、先端から埋めていける。
*/

ll N, u, v, dp[100009][2];
vi edges[100009];

void dfs(int x, int last = -1) {
    dp[x][0] = dp[x][1] = 1;
    for (auto to : edges[x]) {
        // 木を下る方向にしか注目していないので、登る方向の辺は continue する
        // この操作によって今回の木を DAG(有向非循環グラフ)として扱えるようになる
        if (to == last)
            continue;
        dfs(to, x);
        dp[x][0] = dp[x][0] * ((dp[to][0] + dp[to][1]) % MOD) % MOD;
        dp[x][1] = dp[x][1] * dp[to][0] % MOD;
    }
}

int main() {
    cin >> N;
    for (int i = 0; i < N - 1; i++) {
        cin >> u >> v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }
    dfs(1);
    cout << (dp[1][0] + dp[1][1]) % MOD << endl;
    return 0;
}