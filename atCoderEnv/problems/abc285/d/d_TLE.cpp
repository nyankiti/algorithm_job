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

int main() {
  int N;
  static string S[100009], T[100009];
  cin >> N;
  rep(i, 1, N + 1) cin >> S[i] >> T[i];
  map<string, bool> reserved;
  deque<pair<int, string>> deq;

  rep(i, 1, N + 1) {
    reserved[S[i]] = true;
    deq.push_back(make_pair(i, T[i]));
  }

  // とりあえず、変更可能な人から変更していき、デッドロックになったら脱出する
  int current_loop = 0;
  while (!deq.empty()) {
    pair<int, string> next_target = deq.front();
    deq.pop_front();
    if (reserved[next_target.second]) {
      if (current_loop == deq.size()) {
        break;
      }
      deq.push_back(next_target);
      current_loop += 1;
    } else {
      // 新しく利用される名前を予約
      reserved[next_target.second] = true;
      // 前まで利用していた名前の予約の解除
      reserved[S[next_target.first]] = false;

      current_loop = 0;
    }
  }

  cout << (deq.empty() ? "Yes" : "No") << endl;

  return 0;
}