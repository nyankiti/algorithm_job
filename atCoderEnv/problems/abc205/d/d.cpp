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
    int N, Q;
    cin >> N >> Q;
    ll K;
    vector<ll> A(N), exclude_count(N);
    map<ll, int> visited; // 値、indexを持たせる
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    exclude_count[0] = A[0] - 1;
    for (int i = 1; i < N; i++) {
        exclude_count[i] = exclude_count[i - 1] + (A[i] - A[i - 1] - 1);
    }

    for (int i = 0; i < N; i++) {
        cout << exclude_count[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < Q; i++) {
        cin >> K;
        auto itr = lower_bound(exclude_count.begin(), exclude_count.end(), K);
        int r = itr - exclude_count.begin();
        ll ans;
        if (r == 0) {
            ans = K;
        } else {
            ans = A[r - 1] + (K - exclude_count[r - 1]);
        }
        cout << ans << endl;
        cout << r << " " << exclude_count[r - 1] << endl;
    }
    return 0;
}