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
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int main() {
    string S;
    cin >> S;
    rep(i, 0, S.size()) {
        if (isupper(S[i])) {
            cout << i + 1 << endl;
            break;
        }
    }
    return 0;
}