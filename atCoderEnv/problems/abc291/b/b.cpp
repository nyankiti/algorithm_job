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
    int N, x;
    vi X;
    cin >> N;
    rep(i, 1, 5 * N + 1) {
        cin >> x;
        X.push_back(x);
    }
    int temp_sum = accumulate(X.begin(), X.end(), 0);
    sort(X.begin(), X.end());
    rep(i, 0, N) temp_sum -= X[i];
    reverse(X.begin(), X.end());
    rep(i, 0, N) temp_sum -= X[i];
    double ans = temp_sum / (double)(3 * N);
    cout << ans << endl;
    return 0;
}