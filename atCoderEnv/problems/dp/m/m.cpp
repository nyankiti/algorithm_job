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

int N, K, a[100009], MOD = 1000000007;
int main() {
    static int dp[109][100009], ruiseki[109][100009];
    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        cin >> a[i];
    }

    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= K; j++) {
            dp[i][j] = 0;
            ruiseki[i][j] = 0;
        }
    }

    dp[0][0] = 1;

    for (int j = 0; j <= K; j++) {
        ruiseki[0][j] = 1;
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 0; j <= K; j++) {
            // ここを累積和で計算量を改善する必要がある
            // for (int k = 0; k <= a[i]; k++) {
            //     dp[i][j] += dp[i - 1][j - k];
            //     dp[i][j] %= MOD;
            // }
            // dp[i][j] += (ruiseki[i - 1][j] - ruiseki[i - 1][j - a[i] - 1));
            dp[i][j] = ruiseki[i - 1][j];
            if (j - a[i] - 1 >= 0)
                dp[i][j] -= ruiseki[i - 1][j - a[i] - 1];
            dp[i][j] %= MOD;
        }
        // 次のために i 行目の累積和を計算する
        ruiseki[i][0] = dp[i][0];
        for (int j = 1; j <= K; j++) {
            ruiseki[i][j] = ruiseki[i][j - 1] + dp[i][j];
            ruiseki[i][j] %= MOD;
        }
    }
    if (dp[N][K] < 0)
        dp[N][K] += MOD;
    cout << dp[N][K] << endl;

    return 0;
}