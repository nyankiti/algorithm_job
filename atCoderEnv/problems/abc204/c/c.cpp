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

int N, M, A, B;
int main() {
    cin >> N >> M;
    vector<vector<int>> graph(N, vector<int>());

    for (int i = 0; i < M; i++) {
        cin >> A >> B;
        A--;
        B--;
        graph[A].push_back(B);
    }

    int ans = 0;
    for (int i = 0; i < N; i++) {
        int start = i;
        queue<int> q;
        vector<bool> visited(N, false);
        q.push(start);
        visited[start] = true;
        ans += 1;
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            for (int adj : graph[curr]) {
                if (!visited[adj]) {
                    visited[adj] = true;
                    q.push(adj);
                    ans += 1;
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}
