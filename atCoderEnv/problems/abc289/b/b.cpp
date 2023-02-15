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
int N, M, A[109];
bool visited[109];
int main() {
  cin >> N >> M;
  UnionFind uf = UnionFind(N);
  rep(i, 0, N) visited[i] = false;

  rep(i, 1, M + 1) {
    cin >> A[i];
    A[i]--;
    uf.unite(A[i], A[i] + 1);
  }
  rep(i, 0, N) {
    if (visited[i] == false) {
      // A[i]が属するグループを大きい順で出力
      vi temp;
      int group_parent = uf.find(i);
      rep(j, 0, N) {
        if (uf.find(j) == group_parent) {
          temp.push_back(j);
        }
      }
      sort(temp.begin(), temp.end());
      reverse(temp.begin(), temp.end());
      for (int val : temp) {
        cout << val + 1 << " ";
        visited[val] = true;
      }
    }
  }
  cout << endl;
  return 0;
}