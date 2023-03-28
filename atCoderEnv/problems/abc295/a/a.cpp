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

int N;
string W[109];
int main() {
    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> W[i];
    map<string, bool> m({
        {"and", true},
        {"not", true},
        {"that", true},
        {"the", true},
        {"you", true},
    });
    for (int i = 1; i <= N; i++) {
        if (m[W[i]]) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}