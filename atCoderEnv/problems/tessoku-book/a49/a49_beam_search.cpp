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

struct State {
  int score;
  int X[29];
  char last_move;
  int last_pos;
};

// > 演算子のオーバーロード
bool operator>(const State& a1, const State& a2) {
  if (a1.score > a2.score)
    return true;
  else
    return false;
}

int T, P[109], Q[109], R[109];
const int WIDTH = 10000;  // ビーム幅
const int N = 20;
int num_state[109];  // i手目の状態数
State beam[109][WIDTH];
char answer[109];

void beam_search() {
  // 0手目の状態を設定
  num_state[0] = 1;
  beam[0][0].score = 0;
  rep(i, 1, N + 1) beam[0][0].X[i] = 0;

  // ビームサーチ
  rep(i, 1, T + 1) {
    vector<State> candidate;
    rep(j, 0, num_state[i - 1]) {
      // 操作 A の場合
      State sousaA = beam[i - 1][j];
      sousaA.last_move = 'A';
      sousaA.last_pos = j;
      sousaA.X[P[i]] += 1;
      sousaA.X[Q[i]] += 1;
      sousaA.X[R[i]] += 1;
      rep(k, 1, N + 1) {
        if (sousaA.X[k] == 0) sousaA.score += 1;
      }

      // 操作 B の場合
      State sousaB = beam[i - 1][j];
      sousaB.last_move = 'B';
      sousaB.last_pos = j;
      sousaB.X[P[i]] -= 1;
      sousaB.X[Q[i]] -= 1;
      sousaB.X[R[i]] -= 1;
      rep(k, 1, N + 1) {
        if (sousaB.X[k] == 0) sousaA.score += 1;
      }

      // 候補に追加
      candidate.push_back(sousaA);
      candidate.push_back(sousaB);
    }

    // ソートしてbeam[i]の結果を計算する
    // (ここでgreater演算子で比較できるように、Stateの >
    // 演算子をオーバーロードした)
    sort(candidate.begin(), candidate.end(), greater<State>());
    num_state[i] = min(WIDTH, (int)candidate.size());
    rep(j, 0, num_state[i]) beam[i][j] = candidate[j];
  }
}

int main() {
  cin >> T;
  rep(i, 1, T + 1) cin >> P[i] >> Q[i] >> R[i];
  // ビームサーチ
  beam_search();

  int current_place = 0;
  for (int i = T; i >= 1; i--) {
    answer[i] = beam[i][current_place].last_move;
    current_place = beam[i][current_place].last_pos;
  }
  rep(i, 1, T + 1) cout << answer[i] << endl;
  return 0;
}