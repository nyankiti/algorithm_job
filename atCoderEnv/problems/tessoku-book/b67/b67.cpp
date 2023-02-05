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

int N, M, A[100009], B[100009], C[100009];
vector<pii> G[100009];
int main() {
  cin >> N >> M;
  vector<pii> edge_list;
  rep(i, 0, M) {
    cin >> A[i] >> B[i] >> C[i];
    edge_list.push_back(make_pair(C[i], i));
  }
  // 辺を大きい順にソート
  // sort(edge_list.begin(), edge_list.end(),
  //      [](pii x, pii y) { return x.first > y.first; });
  sort(edge_list.begin(), edge_list.end());
  reverse(edge_list.begin(), edge_list.end());

  // 辺が小さい順に追加していく
  UnionFind uf = UnionFind(N);
  int edge_count = 0, edge_idx = 0, ans = 0;
  while (edge_count != N - 1) {
    int edge_id, edge_cost;
    tie(edge_cost, edge_id) = edge_list[edge_idx];
    if (!uf.is_same(A[edge_id] - 1, B[edge_id] - 1)) {
      edge_count += 1;
      ans += edge_cost;
      uf.unite(A[edge_id] - 1, B[edge_id] - 1);
    }
    edge_idx += 1;
  }
  cout << ans << endl;
  return 0;
}