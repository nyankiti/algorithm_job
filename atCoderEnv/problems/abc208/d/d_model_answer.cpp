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

int main() {
    int N, M, A, B, C;
    cin >> N >> M;

    // ワーシャルフロイド法で管理する辺の距離
    vector<vector<int>> dist(N, vector<int>(N, INF));
    for (int i = 0; i < N; i++)
        dist[i][i] = 0;

    for (int i = 0; i < M; i++) {
        cin >> A >> B >> C;
        A--;
        B--;
        dist[A][B] = C;
    }
    ll ans = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k < N; k++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                if (dist[i][j] != INF)
                    ans += dist[i][j];
            }
    cout << ans << endl;
    return 0;
}
