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

string S;
bool check(string candidate) {
    for (int i = 0; i < S.size(); i++) {
        char ch_i = i + '0';
        if (S[i] == 'o') {
            // candidateの S[i]を含む必要がある
            bool is_include = false;
            for (char val : candidate) {
                if (ch_i == val) {
                    is_include = true;
                }
            }
            if (is_include == false)
                return false;

        } else if (S[i] == 'x') {
            // candidateの S[i]が含まれてはいけない
            for (char val : candidate) {
                if (ch_i == val) {
                    return false;
                }
            }
        }
    }
    return true;
}
int main() {
    cin >> S;
    int ans = 0;
    // 全探索する
    for (int i = 0; i < 10000; i++) {
        ostringstream oss;
        oss << setw(4) << setfill('0') << i;
        string candidate = oss.str();
        if (check(candidate))
            ans += 1;
    }
    cout << ans << endl;

    return 0;
}