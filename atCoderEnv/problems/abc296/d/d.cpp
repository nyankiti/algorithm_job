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

// 答えで二分探索 => 答えは
int main() {
    ll N;
    double M;
    ll ans = 1e18;
    cin >> N >> M;
    for (ll a = 1; a <= ceil(sqrt(M)); a++) {
        ll b = (M + a - 1) / a;
        if (a <= N && b <= N) {
            ans = min(ans, a * b);
        }
    }
    if (ans == 1e18) {
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }
    return 0;
}