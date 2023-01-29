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

int N = 100, Q = 1000, A[109][109], B[109][109];
int X[1009], Y[1009], H[1009];

// L 以上 R 以下のランダムな整数を返す関数
int RandInt(int L, int R) { return rand() % (R - L + 1) + L; }

int get_score() {
  int sum = 0;
  rep(i, 0, N) rep(j, 0, N) sum += abs(A[i][j] - B[i][j]);
  return 200000000 - sum;
}
// X[t]=x, Y[t]=y, H[t]=h に変更する関数
void change(int t, int x, int y, int h) {
  rep(i, 0, N) {
    rep(j, 0, N) { B[j][i] -= max(0, H[t] - abs(X[t] - i) - abs(Y[t] - j)); }
  }
  X[t] = x;
  Y[t] = y;
  H[t] = h;
  rep(i, 0, N) {
    rep(j, 0, N) { B[j][i] += max(0, H[t] - abs(X[t] - i) - abs(Y[t] - j)); }
  }
}

void yamanobori() {
  // 変数の設定（5.95 秒ループを回す）
  int TIMELIMIT = 5.95 * CLOCKS_PER_SEC;
  int current_score = get_score();
  int ti = clock();

  // 山登り法スタート
  while (clock() - ti < TIMELIMIT) {
    int t = RandInt(1, Q);
    int old_x = X[t], new_x = X[t] + RandInt(-9, 9);
    int old_y = Y[t], new_y = Y[t] + RandInt(-9, 9);
    int old_h = H[t], new_h = H[t] + RandInt(-19, 19);
    if (new_x < 0 || new_x >= N) continue;
    if (new_y < 0 || new_y >= N) continue;
    if (new_h <= 0 || new_h > N) continue;

    // とりあえず変更し、スコアを評価する
    change(t, new_x, new_y, new_h);
    int new_score = get_score();

    // スコアに応じて採用／不採用を決める
    if (current_score < new_score)
      current_score = new_score;
    else
      change(t, old_x, old_y, old_h);
  }
}

int main() {
  rep(i, 0, N) rep(j, 0, N) { cin >> A[i][j]; }
  // 初期解を生成
  for (int i = 1; i <= 1000; i++) {
    X[i] = rand() % N;  // 0 以上 N-1 以下のランダムな整数
    Y[i] = rand() % N;  // 0 以上 N-1 以下のランダムな整数
    H[i] = 1;
    B[X[i]][Y[i]] += 1;
  }

  // 山登り法
  yamanobori();

  // 出力
  cout << "1000" << endl;
  for (int i = 1; i <= 1000; i++) {
    cout << X[i] << " " << Y[i] << " " << H[i] << endl;
  }
  return 0;
}