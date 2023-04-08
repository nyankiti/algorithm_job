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
    int N, ans = 0;
    cin >> N;
    vector<int> l(N), r(N);
    for (int i = 0; i < N; i++) {
        int t;
        cin >> t >> l[i] >> r[i];
        l[i] *= 2;
        r[i] *= 2;
        if (t >= 3)
            l[i] += 1;
        if (t % 2 == 0)
            r[i] -= 1;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < i; j++) {
            // 区間が交差しない場合を省く
            if (r[i] < l[j] or r[j] < l[i])
                continue;
            ans += 1;
        }
    }

    cout << ans << endl;
    return 0;
}