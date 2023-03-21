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

int N, a[25][25], MOD = 1000000007;
// dp[s]: 左から bitcnt[s]人の男性と、女性の部分集合 s でマッチングする場合の数
int dp[1 << 21], bitcnt[1 << 21];
int main() {
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> a[i][j];
    dp[0] = 1;
    for (int s = 1; s < (1 << N); s++) {
        // s / 2 することで、bit における最後の一桁以外の値を見ている。最後の一桁は s % 2 することで 1かどうかを判断している
        bitcnt[s] = bitcnt[s / 2] + s % 2;
        for (int lady = 0; lady < N; lady++) {
            // 現在注目している集合 s に、現在注目している lady が含まれない場合は continue する
            if ((s >> lady) % 2 == 0)
                continue;

            dp[s] += dp[s - (1 << lady)] * a[bitcnt[s] - 1][lady];
            dp[s] %= MOD;
        }
    }
    cout << dp[(1 << N) - 1] << endl;

    return 0;
}