#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

class SegmentTree {
 public:
  int data[600009], size = 1;
  void init(int N) {
    size = 1;
    while (size < N) {
      size *= 2;
    }
    rep(i, 1, size * 2 + 1) data[i] = 0;
  }

  void update(int pos, int x) {
    pos = pos + size - 1;
    data[pos] = x;
    while (pos > 1) {
      pos /= 2;
      data[pos] = data[pos * 2] + data[pos * 2 + 1];
    }
  }

  int query(int l, int r, int a, int b, int pos) {
    if (l <= a && b <= r) return data[pos];
    if (b <= l || r <= a) return 0;
    int mid = (a + b) / 2;
    int l_sum = query(l, r, a, mid, pos * 2);
    int r_sum = query(l, r, mid, b, pos * 2 + 1);
    return l_sum + r_sum;
  }
};

int N, A[150009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  SegmentTree sg;
  sg.init(N);
  ll ans = 0;
  rep(j, 1, N + 1) {
    ans += sg.query(A[j] + 1, N + 1, 1, sg.size + 1, 1);
    sg.update(A[j], 1);
  }
  cout << ans << endl;
  return 0;
}