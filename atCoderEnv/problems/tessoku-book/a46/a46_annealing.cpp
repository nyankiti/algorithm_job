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

int N, X[159], Y[159];
int P[159];  // 訪れた都市の順番
bool visited[159];

// a 以上 b 以下の整数をランダムに返す
int rand_ind(int a, int b) { return a + (rand() % (b - a + 1)); }
// 0 以上 1 以下の確率をランダムに返す
double randouble() { return 1.0 * rand() / RAND_MAX; }

double get_dist(int i, int j) {
  return sqrt((X[i] - X[j]) * (X[i] - X[j]) + (Y[i] - Y[j]) * (Y[i] - Y[j]));
}

double get_score() {
  double sum = 0;
  rep(i, 1, N + 1) sum += get_dist(P[i], P[i + 1]);
  return sum;
}

void play_greedy() {
  int current_place = 1;
  // 初期化
  rep(i, 1, N + 1) visited[i] = false;
  P[1] = 1;
  visited[1] = true;
  // 貪欲法スタート(最も近い都市に遷移する)
  rep(i, 2, N + 1) {
    double min_dist = 10000.0;
    int min_id = -1;
    rep(j, 1, N + 1) {
      if (visited[j] == true) continue;
      double new_dist = get_dist(current_place, j);
      if (min_dist > new_dist) {
        min_dist = new_dist;
        min_id = j;
      }
    }
    // その時点での最短の都市を次に訪れる
    P[i] = min_id;
    visited[min_id] = true;
    current_place = min_id;
  }

  // 最後に最初の位置に戻る
  P[N + 1] = 1;
}

int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> X[i] >> Y[i];
  // N = 150 なので、2^N 計算が必要な巡回セールスマン問題は間に合わない

  // Pの初期化
  // rep(i, 1, N + 1) P[i] = i;
  // P[N + 1] = 1;

  // 貪欲法で初期化を行う
  play_greedy();

  // 山登り法
  double current_score = get_score();
  rep(t, 1, 200000) {
    // ランダムに反転させる区間を [L, R] を選ぶ
    int L = rand_ind(2, N);
    int R = rand_ind(2, N);
    if (L > R) swap(L, R);

    // 反転させる
    reverse(begin(P) + L, begin(P) + R + 1);
    double new_score = get_score();
    // 焼きなまし法の温度(終盤ほど悪化する確率が低くなるように調整)
    double T = 30.0 - 28.0 * t / 200000.0;
    double probability = exp(min(0.0, (current_score - new_score) / T));
    if (randouble() < probability)
      current_score = new_score;
    else
      reverse(begin(P) + L, begin(P) + R + 1);
  }
  // 答えの出力
  rep(i, 1, N + 2) cout << P[i] << endl;
  return 0;
}