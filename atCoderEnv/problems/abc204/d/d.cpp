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
int main() {
    cin >> N;
    vector<int> T(N);
    // 部分和が作れるかどうかをdpで保持する(bitsetを用いると超楽)
    bitset<100001> dp;
    dp[0] = 1;
    int tot = 0;
    for (int i = 0; i < N; i++) {
        cin >> T[i];
        tot += T[i];
        dp |= dp << T[i];
    }
    int ans = tot;
    for (int i = 0; i <= tot; i++) {
        if (dp[i]) {
            ans = min(ans, max(i, tot - i));
        }
    }
    cout << ans << endl;

    return 0;
}