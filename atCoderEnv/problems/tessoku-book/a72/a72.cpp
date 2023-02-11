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

int H, W, K;
char C[19][109], temp_grid[19][109];
int main() {
  cin >> H >> W >> K;
  rep(h, 1, H + 1) rep(w, 1, W + 1) cin >> C[h][w];
  int default_black_count = 0;
  rep(h, 1, H + 1) rep(w, 1, W + 1) if (C[h][w] == '#') default_black_count +=
      1;

  vector<pii> h_while_count;
  rep(h, 1, H + 1) {
    h_while_count.push_back(make_pair(h, 0));
    rep(w, 1, W + 1) {
      if (C[h][w] == '.') {
        h_while_count.rbegin()->second += 1;
      }
    }
  }

  // 白の数が大きい順に並び替える
  sort(h_while_count.begin(), h_while_count.end(),
       [](pii o1, pii o2) { return o1.second > o2.second; });
  int ans = 0;
  // 先に h を決めて黒塗りする
  rep(h_select_count, 1, min(K, H) + 1) {
    // 探索のための盤面を初期化
    int temp_ans = default_black_count;
    rep(h, 1, H + 1) rep(w, 1, W + 1) temp_grid[h][w] = C[h][w];

    rep(i, 0, h_select_count) {
      int h = h_while_count[i].first;
      rep(w, 1, W + 1) {
        if (temp_grid[h][w] == '.') {
          temp_ans += 1;
          temp_grid[h][w] = '#';
        }
      }
    }

    // hを決めた後、残りの数で w を決める
    int rest_count = K - h_select_count;
    vector<pii> w_while_count;
    rep(w, 1, W + 1) {
      w_while_count.push_back(make_pair(w, 0));
      rep(h, 1, H + 1) {
        if (temp_grid[h][w] == '.') {
          // 最後の要素のイテレータをrbeginで取得
          w_while_count.rbegin()->second += 1;
        }
      }
    }
    // 白の数が大きい順に並び替える
    sort(w_while_count.begin(), w_while_count.end(),
         [](pii o1, pii o2) { return o1.second > o2.second; });
    rep(i, 0, rest_count) {
      int w = w_while_count[i].first;
      rep(h, 1, H + 1) {
        if (temp_grid[h][w] == '.') {
          temp_ans += 1;
          temp_grid[h][w] = '#';
        }
      }
    }

    ans = max(ans, temp_ans);
  }

  cout << ans << endl;
  return 0;
}