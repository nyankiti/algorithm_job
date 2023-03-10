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

ll divisor_num(ll x) {
    ll ret = 0;
    for (int i = 1; i * i <= x; i++) {
        if (x % i != 0)
            continue;
        if (x / i == i)
            ret += 1;
        else
            ret += 2;
    }
    return ret;
}

int main() {
    int N;
    ll ans = 0;
    cin >> N;

    rep(i, 1, N) {
        int right = i, left = N - i;
        ans += (divisor_num(right)) * (divisor_num(left));
    }
    cout << ans << endl;
    return 0;
}