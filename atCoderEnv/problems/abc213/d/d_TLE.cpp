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

int N, A, B;
vi G[200009];
bool visited[200009];

int main() {
  cin >> N;
  rep(i, 1, N) {
    cin >> A >> B;
    G[A].push_back(B);
    G[B].push_back(A);
  }
  rep(i, 1, N + 1) {
    sort(G[i].begin(), G[i].end());
    visited[i] = false;
  }

  vi ans, prev(N + 1, -1);
  int current = 1;
  visited[1] = true;
  ans.push_back(1);

  while (true) {
    bool is_found = false;
    for (int adj : G[current]) {
      if (visited[adj] == false) {
        if (prev[adj] == -1) {
          prev[adj] = current;
        }
        current = adj;
        ans.push_back(adj);
        visited[adj] = true;
        is_found = true;
        break;
      }
    }
    if (is_found == false) {
      if (current == 1) {
        break;
      } else {
        current = prev[current];
        ans.push_back(current);
      }
    }
  }
  for (int val : ans) cout << val << " ";
  cout << endl;
  return 0;
}