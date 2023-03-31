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

class BIT_max {
public:
    // 大きさだけで初期化する場合
    explicit BIT_max(size_t size) : m_bit(size + 1) {}
    // 閉区間 [1, r) の合計を返す
    ll get_max(int r) {
        ll ret = 0;
        for (; 0 < r; r -= (r & -r)) {
            ret = max(ret, m_bit[r]);
        }
        return ret;
    }
    // i 番目の要素を加算
    void set_val(int idx, ll value) {
        for (; idx < m_bit.size(); idx += (idx & -idx)) {
            m_bit[idx] = max(m_bit[idx], value);
        }
    }

private:
    vector<ll> m_bit;
};

int N, h[200009], a[200009];
// i番目の花を残すとき、iより左の花の美しさの最大値
ll dp[200009];

int main() {
    cin >> N;
    vector<pii> flowers;
    for (int i = 1; i <= N; i++) {
        cin >> h[i];
        flowers.push_back(pii(h[i], i));
    }
    for (int i = 1; i <= N; i++)
        cin >> a[i];

    // h が小さい順に並び替え、BIT(Binary Indexed Tree)を使うことで計算量を削減する
    ll ans = 0;
    sort(flowers.begin(), flowers.end());
    BIT_max bit_max(N + 1);
    for (auto p : flowers) {
        int i = p.second;
        dp[i] = bit_max.get_max(i) + a[i];
        bit_max.set_val(i, dp[i]);
        ans = max(ans, dp[i]);
    }

    cout << ans << endl;
    return 0;
}