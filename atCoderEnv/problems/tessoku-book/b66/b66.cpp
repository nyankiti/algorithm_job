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

class UnionFind {
 public:
  explicit UnionFind(size_t n) : parents(n, -1) {}

  // 頂点 i のrootのインデックスを返す
  int find(int i) {
    if (parents[i] < 0) {
      return i;
    }
    parents[i] = find(parents[i]);
    return parents[i];
  }

  void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
      // union by size(小さい方を子にしてメモリを削減)
      if (parents[a] < parents[b]) swap(a, b);
      parents[a] += parents[b];
      parents[b] = a;
    }
  }

  bool is_same(int a, int b) { return (find(a) == find(b)); }

  int size(int i) { return -parents[find(i)]; }

 private:
  vector<int> parents;
};

int N, M, Q, A[100009], B[100009], type[100009], X[100009], U[100009],
    V[100009];
int main() {
  cin >> N >> M;
  rep(i, 1, M + 1) cin >> A[i] >> B[i];
  cin >> Q;
  map<int, bool> unkyu;
  rep(i, 1, Q + 1) {
    cin >> type[i];
    if (type[i] == 1) {
      cin >> X[i];
      unkyu[X[i]] = true;
    } else if (type[i] == 2) {
      cin >> U[i] >> V[i];
    }
  }

  UnionFind uf = UnionFind(N);
  // 運休になる路線以外をあらかじめ繋げておく
  rep(i, 1, M + 1) {
    if (unkyu[i] == false) {
      uf.unite(A[i], B[i]);
    }
  }
  // 逆から答えを求めていく。
  vector<string> ans;
  for (int i = Q; i > 0; i--) {
    if (type[i] == 1) {
      uf.unite(A[X[i]], B[X[i]]);
    } else {
      if (uf.is_same(U[i], V[i])) {
        ans.push_back("Yes");
      } else {
        ans.push_back("No");
      }
    }
  }
  reverse(ans.begin(), ans.end());
  for (string val : ans) cout << val << endl;

  return 0;
}