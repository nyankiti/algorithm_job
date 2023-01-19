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

  map<string, string> to;
  rep(i, 1, N + 1) to[S[i]] = T[i];
  set<string> used;

  rep(i, 1, N + 1) {
    string start = S[i];
    // 一度訪れたノードはカウントしない
    while (used.count(start) == 0) {
      used.insert(start);
      auto itr = to.find(start);
      // mapのfindメソッドはそのkeyが見つからない場合に末尾のイテレータ(to.end())を返す
      if (itr == to.end()) break;

      // 終点が見つからずに始点に帰ってきた場合はサイクルがあるので、この問題の条件を満たさない
      start = itr->second;
      if (start == S[i]) {
        cout << "No" << endl;
        return 0;
      }
    }
  }
  cout << "Yes" << endl;
  return 0;
}
