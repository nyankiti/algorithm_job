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

int N, K, c[300009];
int main() {
    cin >> N >> K;
    for (int i = 1; i <= N; i++)
        cin >> c[i];
    map<int, int> c_map;
    set<int> c_set;
    int ans = 0;
    // まずK番目までを数える
    for (int i = 1; i < K; i++) {
        c_map[c[i]] += 1;
        c_set.insert(c[i]);
    }

    for (int i = K; i <= N; i++) {
        // 消す
        c_map[c[i - K]] -= 1;
        if (c_map[c[i - K]] == 0) {
            c_set.erase(c[i - K]);
        }
        // 追加する
        c_map[c[i]] += 1;
        c_set.insert(c[i]);

        ans = max(ans, (int)c_set.size());
    }
    cout << ans << endl;
    return 0;
}