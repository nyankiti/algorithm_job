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

int N, A[100009];
int main() {
    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> A[i];
    map<int, int> B_count;
    vector<int> B(N + 1);
    B[0] = -1;
    for (int i = 1; i <= N; i++) {
        cin >> B[i];
        B_count[B[i]] += 1;
    }
    map<int, int> C_count;
    for (int i = 1; i <= N; i++) {
        int C;
        cin >> C;
        C_count[C] += 1;
    }
    sort(B.begin(), B.end());
    // 重複消去
    B.erase(unique(B.begin(), B.end()), B.end());
    int ans = 0;
    for (int i = 1; i <= N; i++) {
        auto itr = lower_bound(begin(B) + 1, begin(B) + N + 1, A[i]);
        if (A[i] == *itr) {
            ans += (C_count[A[i]] * B_count[A[i]]);
        }
    }

    cout << ans << endl;
    return 0;
}