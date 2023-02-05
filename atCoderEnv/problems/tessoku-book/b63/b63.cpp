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

int R, C, dist[59][59];
pii start, goal;
char grid[59][59];
deque<pii> deq;

int main() {
  cin >> R >> C;
  cin >> start.first >> start.second;
  cin >> goal.first >> goal.second;
  rep(r, 1, R + 1) rep(c, 1, C + 1) {
    cin >> grid[r][c];
    dist[r][c] = -1;
  }
  dist[start.first][start.second] = 0;
  deq.push_back(start);
  while (!deq.empty()) {
    pii popped = deq.front();
    int r, c;
    tie(r, c) = popped;
    deq.pop_front();
    // 上
    if (grid[r - 1][c] == '.' && dist[r - 1][c] == -1) {
      dist[r - 1][c] = dist[r][c] + 1;
      deq.push_back(make_pair(r - 1, c));
    }
    // 下
    if (grid[r + 1][c] == '.' && dist[r + 1][c] == -1) {
      dist[r + 1][c] = dist[r][c] + 1;
      deq.push_back(make_pair(r + 1, c));
    }
    // 右
    if (grid[r][c + 1] == '.' && dist[r][c + 1] == -1) {
      dist[r][c + 1] = dist[r][c] + 1;
      deq.push_back(make_pair(r, c + 1));
    }
    // 左
    if (grid[r][c - 1] == '.' && dist[r][c - 1] == -1) {
      dist[r][c - 1] = dist[r][c] + 1;
      deq.push_back(make_pair(r, c - 1));
    }
  }
  cout << dist[goal.first][goal.second] << endl;

  return 0;
}