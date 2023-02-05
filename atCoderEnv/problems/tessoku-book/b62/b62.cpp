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

int N, M, a, b;
vi G[100009];
bool visited[100009];
deque<int> s;

void dfs(int v) {
  visited[v] = true;

  if (v == N) {
    for (auto itr = s.begin(); itr != s.end(); itr++) {
      cout << *itr << " ";
    }
    cout << endl;
    return;
  }
  for (int adj : G[v]) {
    if (visited[adj] == false) {
      s.push_back(adj);
      dfs(adj);
      s.pop_back();
    }
  }
  return;
}
int main() {
  cin >> N >> M;
  rep(i, 0, M) {
    cin >> a >> b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  rep(i, 1, N + 1) visited[i] = false;
  s.push_back(1);
  dfs(1);
  return 0;
}