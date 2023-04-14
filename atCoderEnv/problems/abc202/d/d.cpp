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

// コンビネーションをあらかじめパスカルの三角形を利用して計算しておく
ll comb[61][61];

int main() {
    ll A, B, K;
    cin >> A >> B >> K;

    comb[0][0] = 1;
    for (int i = 0; i < 60; i++) {
        for (int j = 0; j <= i; j++) {
            comb[i + 1][j] += comb[i][j];
            comb[i + 1][j + 1] += comb[i][j];
        }
    }

    string ans;
    while (A + B > 0) {
        // ここまでの先頭をAとした場合、何通りあるか
        ll x = 0;
        if (A >= 0)
            x = comb[A + B - 1][A - 1];
        if (K <= x) {
            ans += 'a';
            A -= 1;
        } else {
            ans += 'b';
            B -= 1;
            K -= x;
        }
    }
    cout << ans << endl;

    return 0;
}
