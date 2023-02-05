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
struct Edge {
  // to: 行き先, cap: 容量, rev: 行き先から見た自分の番号
  int to, cap, rev;
};
class MaximumFlow {
 public:
  // 最初の変数はメンバー初期化リストの記法を用いて設定する
  explicit MaximumFlow(int n) : size(n), used(n + 1, false), G(n + 1) {}

  void add_edge(int a, int b, int c) {
    int current_Ga = G[a].size();  // 現時点でのG[a]の要素数
    int current_Gb = G[b].size();  // 現時点でのG[b]の要素数
    G[a].push_back(Edge({b, c, current_Gb}));
    G[b].push_back(Edge({a, 0, current_Ga}));
  }

  // F はスタートからposに到達する過程での残余グラフの辺の容量の最小値
  int dfs(int pos, int goal, int F) {
    if (pos == goal) return F;
    used[pos] = true;
    // 探索
    for (int i = 0; i < G[pos].size(); i++) {
      // 容量 0 の辺は扱えない
      if (G[pos][i].cap == 0) continue;

      // 既に訪問んした頂点にはいかない
      if (used[G[pos][i].to] == true) continue;

      // 目的地までのパスを探す
      int flow = dfs(G[pos][i].to, goal, min(F, G[pos][i].cap));

      if (flow >= 1) {
        G[pos][i].cap -= flow;
        G[G[pos][i].to][G[pos][i].rev].cap += flow;
        return flow;
      }
    }
    // 全ての辺を探索しても見つからなかった場合
    return 0;
  }

  int max_flow(int start, int goal) {
    int total_flow = 0;
    while (true) {
      for (int i = 0; i <= size; i++) used[i] = false;
      int F = dfs(start, goal, 1000000000);

      // 流せなくなったら終了
      if (F == 0) break;

      total_flow += F;
    }
    return total_flow;
  }

 private:
  int size;
  vector<bool> used;
  vector<vector<Edge>> G;
};

int N, M, a, b, c;
int main() {
  cin >> N >> M;
  MaximumFlow mf = MaximumFlow(N);
  rep(i, 0, M) {
    cin >> a >> b >> c;
    mf.add_edge(a, b, c);
  }
  cout << mf.max_flow(1, N) << endl;
  return 0;
}