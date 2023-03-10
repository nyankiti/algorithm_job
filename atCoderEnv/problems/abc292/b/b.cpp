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

int N, Q;
int main() {
    cin >> N >> Q;
    map<int, int> cards;

    rep(i, 0, Q) {
        int type, x;
        cin >> type >> x;
        if (type == 1) {
            cards[x] += 1;
        } else if (type == 2) {
            cards[x] += 2;
        } else {
            cout << (cards[x] >= 2 ? "Yes" : "No") << endl;
        }
    }
    return 0;
}