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

int N, A[200009];
int main() {
    cin >> N;
    map<int, bool> called;
    rep(i, 1, N + 1) called[i] = false;
    rep(i, 1, N + 1) {
        cin >> A[i];
        if (called[i] == false) {
            called[A[i]] = true;
        }
    }
    vi ans;
    for (auto itr = called.begin(); itr != called.end(); itr++) {
        if (itr->second == false)
            ans.push_back(itr->first);
    }
    cout << ans.size() << endl;
    for (auto val : ans)
        cout << val << " ";

    return 0;
}