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

ll N, K;
int main() {
    cin >> N >> K;
    vector<vector<ll>> a(N);
    for (int i = 0; i < N; i++) {
        int val;
        cin >> val;
        a[i] = {val, i, 0};
    }
    sort(a.begin(), a.end());
    ll rest = K % N, quotient = K / N;

    int i = 1;
    while (i <= rest) {
        a[i - 1][2] += 1;
        i++;
    }

    // 2番めの値で並び替える
    sort(a.begin(), a.end(), [](const vector<ll> &a, const vector<ll> &b) {
        return (a[1] < b[1]);
    });
    for (int i = 0; i < N; i++) {
        cout << a[i][2] + quotient << endl;
    }
    return 0;
}
