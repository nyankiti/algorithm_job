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

int N, M, A, B;
int main() {
  cin >> N >> M;
  UnionFind uf = UnionFind(N + 1);
  int ans = 0;
  rep(i, 1, M + 1) {
    cin >> A >> B;
    if (!uf.is_same(A, B)) {
      uf.unite(A, B);
    } else {
      ans += 1;
    }
  }
  cout << ans << endl;
  return 0;
}