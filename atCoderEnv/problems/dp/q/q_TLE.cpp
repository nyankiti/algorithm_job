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

int N, h[200009], a[200009];
// i番目の花を残すとき、iより左の花の美しさの最大値
ll dp[200009];
int main() {
    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> h[i];
    for (int i = 1; i <= N; i++)
        cin >> a[i];
    for (int i = 1; i <= N; i++)
        dp[i] = 0;

    for (int i = 1; i <= N; i++) {
        dp[i] = a[i];
        for (int j = i - 1; j > 0; j--) {
            // i番目の花を残すことは確定しているので、i番目を選ばない場合は考えない
            if (h[i] > h[j]) {
                dp[i] = max(dp[i], dp[j] + a[i]);
            }
        }
    }

    cout << dp[N] << endl;
    return 0;
}