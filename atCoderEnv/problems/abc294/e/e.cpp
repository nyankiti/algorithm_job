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

ll L, l;
int N_1, N_2, v;
int main() {
    cin >> L >> N_1 >> N_2;
    deque<pair<int, ll>> A, B;
    for (int i = 1; i <= N_1; i++) {
        cin >> v >> l;
        A.push_back({v, l});
    }
    for (int i = 1; i <= N_2; i++) {
        cin >> v >> l;
        B.push_back({v, l});
    }
    ll current_pos = 0, A_pos = 0, B_pos = 0, ans = 0;
    while (current_pos < L) {
        if (A_pos + A.front().second < B_pos + B.front().second) {
            if (A.front().first == B.front().first) {
                ans += (A_pos + A.front().second - current_pos);
            }
            A_pos += A.front().second;
            current_pos = A_pos;
            A.pop_front();
        } else {
            if (A.front().first == B.front().first) {
                ans += (B_pos + B.front().second - current_pos);
            }
            B_pos += B.front().second;
            current_pos = B_pos;
            B.pop_front();
        }
    }
    cout << ans << endl;
    return 0;
}