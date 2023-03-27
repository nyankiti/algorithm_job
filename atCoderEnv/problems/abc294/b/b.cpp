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

int H, W, A[109][109];
int main() {
    cin >> H >> W;
    for (int i = 1; i <= H; i++)
        for (int j = 1; j <= W; j++)
            cin >> A[i][j];

    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            if (A[i][j] == 0)
                cout << '.';
            else
                cout << char(A[i][j] + 64);
        }
        cout << endl;
    }

    return 0;
}
