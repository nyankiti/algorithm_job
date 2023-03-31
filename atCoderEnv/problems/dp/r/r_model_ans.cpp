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

struct Matrix {
    ll val[50][50];
    Matrix() {
        for (int i = 0; i < 50; i++)
            for (int j = 0; j < 50; j++)
                val[i][j] = 0;
    }
};
Matrix operator*(Matrix a, Matrix b) {
    Matrix c;
    for (int i = 0; i < 50; i++)
        for (int j = 0; j < 50; j++)
            for (int k = 0; k < 50; k++) {
                c.val[i][j] += a.val[i][k] * b.val[k][j] % MOD;
                c.val[i][j] %= MOD;
            }
    return c;
}
// 単位行列
Matrix I;

// 繰り返し二乗法で累乗を計算する
Matrix matrix_power(Matrix a, ll k) {
    if (k == 0)
        return I;
    Matrix res = matrix_power(a, k / 2);
    res = res * res;
    if (k % 2 == 1)
        res = res * a;
    return res;
}

int N;
ll K;
int main() {
    // 単位行列の初期化
    for (int i = 0; i < 50; i++)
        I.val[i][i] = 1;

    cin >> N >> K;
    Matrix A;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> A.val[i][j];
    // Aのk乗を計算する
    Matrix A_k = matrix_power(A, K);
    ll ans = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            ans += A_k.val[i][j];
            ans %= MOD;
        }

    cout << ans << endl;

    return 0;
}