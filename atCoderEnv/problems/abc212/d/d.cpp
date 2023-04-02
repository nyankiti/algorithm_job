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

int main() {
    int Q, P;
    ll x;
    cin >> Q;
    // multiset<ll> ms;
    priority_queue<ll, vector<ll>, greater<ll>> pq;
    ll diff = 0;
    for (int i = 1; i <= Q; i++) {
        cin >> P;
        if (P == 1) {
            cin >> x;
            pq.push(x - diff);
            // ms.insert(x - diff);
        } else if (P == 2) {
            cin >> x;
            diff += x;
        } else {
            ll mini_ball = pq.top();
            pq.pop();
            cout << mini_ball + diff << endl;
            // cout << *ms.begin() + diff << endl;
            // ms.erase(ms.begin());
        }
    }
    return 0;
}