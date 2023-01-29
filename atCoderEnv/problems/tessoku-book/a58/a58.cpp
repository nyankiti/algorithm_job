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
  int data[300000], size = 1;

  void init(int N) {
    size = 1;
    // N を超える最小の 2 の累乗がサイズとなる
    while (size < N) size *= 2;
    rep(i, 1, size * 2) data[i] = 0;
  }

  void update(int pos, int x) {
    pos = pos + size - 1;
    data[pos] = x;
    while (pos >= 2) {
      pos /= 2;
      data[pos] = max(data[pos * 2], data[pos * 2 + 1]);
    }
  }

  int query(int l, int r, int a, int b, int u) {
    if (r <= a || b <= l) return -1000000000;
    if (l <= a && b <= r) return data[u];  // 完全に含まれる場合
    int m = (a + b) / 2;
    int ans_l = query(l, r, a, m, u * 2);
    int ans_r = query(l, r, m, b, u * 2 + 1);
    return max(ans_l, ans_r);
  }
};

int N, Q;
int main() {
  cin >> N >> Q;

  SegmentTree sg;
  sg.init(N);

  rep(i, 0, Q) {
    int type;
    cin >> type;
    if (type == 1) {
      int pos, x;
      cin >> pos >> x;
      sg.update(pos, x);
    } else {
      int l, r;
      cin >> l >> r;
      cout << sg.query(l, r, 1, sg.size + 1, 1) << endl;
    }
  }
  return 0;
}