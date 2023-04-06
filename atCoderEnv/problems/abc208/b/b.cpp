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
    int P, factorial[19];
    cin >> P;
    // factorialを計算する
    factorial[1] = 1;
    for (int i = 2; i <= 10; i++) {
        factorial[i] = factorial[i - 1] * i;
    }
    // カウントを作る
    map<int, int> fact_cnt;
    for (int i = 1; i <= 10; i++) {
        fact_cnt[i] = 100;
    }
    int ans = 0, i = 10;
    while (P >= 0 && i > 0) {
        if (P >= factorial[i] && fact_cnt[i] > 0) {
            P -= factorial[i];
            fact_cnt[i] -= 1;
            ans += 1;
        } else {
            i -= 1;
        }
    }
    cout << ans << endl;
    return 0;
}