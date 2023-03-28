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
int R, C;
char B[29][29];

void explode_bomb(int power, int i, int j) {
    for (int k = 1; k <= R; k++)
        for (int l = 1; l <= C; l++) {
            if (abs(i - k) + abs(j - l) <= power && !isdigit(B[k][l])) {
                B[k][l] = '.';
            }
        }
}
int main() {
    cin >> R >> C;
    for (int i = 1; i <= R; i++)
        for (int j = 1; j <= C; j++)
            cin >> B[i][j];

    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            if (isdigit(B[i][j])) {
                int power = (int)B[i][j] - (int)'0';
                // マンハッタン距離いないのマスを変更する
                explode_bomb(power, i, j);
                B[i][j] = '.';
            }
        }
    }

    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            cout << B[i][j];
        }
        cout << endl;
    }

    return 0;
}