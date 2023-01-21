#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvl = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

class UnionFind {
 public:
  /*
     size_tはサイズを表す型。整数しか取れない。intで代用することもできるが、
     明示的に何かのサイズであることを表すことができ、可読性、安全性が高まるというメリットがある。
     size_t型の最大値は環境によって異なり、SIZE_MAXによって確かめることができる

     parentsの初期値はメンバ初期化リストによって更新する
  */
  explicit UnionFind(size_t n) : parents(n, -1) {}

  // 参考にした記事にはデフォルトコンストラクタを書いていたが、いらない気がする
  // UnionFind() = default;

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
int main() {
  UnionFind uf(9);
  return 0;
}