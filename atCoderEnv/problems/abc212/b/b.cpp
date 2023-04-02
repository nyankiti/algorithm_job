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

string X;
bool is_weak() {
    int cnt = count(X.begin(), X.end(), X[0]);
    if (cnt == 4) {
        return true;
    }
    bool res = true;
    for (int i = 0; i <= 2; i++) {
        int num = X[i] - '0';
        int next_num = X[i + 1] - '0';
        if ((num + 1) % 10 != next_num % 10) {
            res = false;
        }
    }
    return res;
}
int main() {
    cin >> X;
    cout << (is_weak() ? "Weak" : "Strong") << endl;
    return 0;
}