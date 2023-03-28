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
/*
嬉しい列同士が隣り合う場合は嬉しい列。
奇数の数列は決して嬉しい数列にはならない。(嬉しい数列が含まれる場合はある)
=> 最初に作った嬉しい数列をいい感じに成長させていくことでDPできそう
*/
string S;
int ruiseki_table[19][500009];
int main() {
    cin >> S;
    ll ans = 0;
    int N = S.size();
    // ruiseki table を作る
    for (int i = 0; i < N; i++) {
        int x = S[i] - '0';
        for (int j = 0; j < 10; j++) {
            if (j == x) {
                ruiseki_table[x][i + 1] = ruiseki_table[x][i] + 1;
            } else {
                ruiseki_table[j][i + 1] = ruiseki_table[j][i];
            }
        }
    }
    // 0(N^2)で探索する
    for (int i = 1; i <= N; i++) {
        for (int j = i + 1; j <= N; j++) {
            int flg = true;
            for (int k = 0; k < 10; k++) {
                if ((ruiseki_table[k][j] - ruiseki_table[k][i - 1]) % 2 != 0) {
                    flg = false;
                }
            }
            if (flg) {
                ans += 1;
            }
        }
    }
    cout << ans << endl;
    return 0;
}