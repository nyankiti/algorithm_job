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
    ll N;
    cin >> N;
    vi A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    ll ans = (N - 1) * N / 2;

    map<int, ll> cnt;
    for (int i = 0; i < N; i++) {
        cnt[A[i]]++;
    }
    for (auto itr = cnt.begin(); itr != cnt.end(); itr++) {
        ans -= (itr->second * (itr->second - 1) / 2);
    }

    cout << ans << endl;
    return 0;
}