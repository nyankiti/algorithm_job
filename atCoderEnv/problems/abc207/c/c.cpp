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

bool check(int t1, int l1, int r1, int t2, int l2, int r2) {
    if (t1 == 2) {
        r1 -= 1;
    } else if (t1 == 3) {
        l1 += 1;
    } else if (t1 == 4) {
        l1 += 1;
        r1 -= 1;
    }

    if (t2 == 2) {
        r2 -= 1;
    } else if (t2 == 3) {
        l2 += 1;
    } else if (t2 == 4) {
        l2 += 1;
        r2 -= 1;
    }

    // かぶっていない
    if (r1 < l2 or r2 < l1) {
        return false;
    } else {
        return true;
    }
    // 1が内側、2が外側の時
    // else if (l2 < l1 & r1 < r2) {
    //     return true;
    // }
    // // 2が内側、1が外側の時
    // else if (l1 < l2 & r2 < r1) {
    //     return true;
    // } else {
    //     return true;
    // }
}

int main() {
    int N, t, l, r;
    cin >> N;
    vector<tuple<int, int, int>> kukan;
    for (int i = 0; i < N; i++) {
        cin >> t >> l >> r;
        kukan.push_back({t, l, r});
    }
    int t1, l1, r1, t2, l2, r2;
    int ans = 0;
    for (int i = 0; i < N; i++) {
        tie(t1, l1, r1) = kukan[i];
        for (int j = 0; j < i; j++) {
            tie(t2, l2, r2) = kukan[j];
            if (check(t1, l1 * 2, r1 * 2, t2, l2 * 2, r2 * 2)) {
                ans += 1;
            }
        }
    }
    cout << ans << endl;
    return 0;
}