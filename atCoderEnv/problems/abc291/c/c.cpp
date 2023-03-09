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
    int N;
    string S;
    cin >> N >> S;
    set<pii> visited;
    int x = 0, y = 0;
    visited.insert(make_pair(x, y));
    for (char val : S) {
        if (val == 'R')
            x += 1;
        if (val == 'L')
            x -= 1;
        if (val == 'U')
            y += 1;
        if (val == 'D')
            y -= 1;
        if (visited.count(make_pair(x, y))) {
            cout << "Yes" << endl;
            return 0;
        }
        visited.insert(make_pair(x, y));
    }
    cout << "No" << endl;
    return 0;
}