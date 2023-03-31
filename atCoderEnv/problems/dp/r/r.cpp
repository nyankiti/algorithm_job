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

class SquareMatrix {
private:
    vector<vector<ll>> data;
    size_t size;

public:
    // 大きさだけで初期化する場合
    explicit SquareMatrix(size_t N) : data(N, vector<ll>(N)), size(N) {}
    // 行列で初期化する場合
    explicit SquareMatrix(const vector<vector<ll>> &data) : size(data.size()), data(data) {}

    ll get(int i, int j) { return data[i][j]; }
    void set(int i, int j, ll val) { data[i][j] = val; }

    SquareMatrix operator*(const SquareMatrix &other) {
        SquareMatrix newData(size);
        for (int i = 0; i < size; i++)
            for (int j = 0; j < size; j++) {
                ll temp_sum = 0;
                for (int k = 0; k < size; k++) {
                    temp_sum += this->data[i][k] * other.data[k][j] % MOD;
                    temp_sum %= MOD;
                }
                newData.set(i, j, temp_sum);
            }
        return newData;
    }

    // 繰り返し二乗法で累乗を計算する
    SquareMatrix power(ll k) {
        if (k == 0) {
            // 単位行列を返す
            SquareMatrix I(size);
            for (int i = 0; i < size; i++)
                I.set(i, i, 1);
            return I;
        }
        SquareMatrix res = this->power(k / 2);
        res = res * res;
        if (k % 2 == 1) {
            SquareMatrix my_instance = *this;
            res = res * my_instance;
        }
        return res;
    }
};

int N;
ll K;
int main() {
    cin >> N >> K;

    SquareMatrix A(N);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            int val;
            cin >> val;
            A.set(i, j, val);
        }

    // Aのk乗を計算する
    SquareMatrix A_k = A.power(K);
    ll ans = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            ans += A_k.get(i, j);
            ans %= MOD;
        }

    cout << ans << endl;

    return 0;
}