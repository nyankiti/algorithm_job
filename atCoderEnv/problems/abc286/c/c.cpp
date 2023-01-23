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

int N;
ll A, B;
string S;
int main() {
  cin >> N >> A >> B >> S;
  // とりあえず一周まわして、最も回文に近い並びを探索する
  ll score = 100000000000000;
  rep(i, 0, N) {
    // 回文への近さのスコアを算出する
    ll temp_score = A * i;
    rep(j, 0, N / 2) {
      if (S[j] != S[N - j - 1]) {
        temp_score += B;
      }
    }
    // cout << S << " " << temp_score << endl;
    score = min(score, temp_score);

    char poped = S.front();
    S.push_back(poped);
    S.erase(0, 1);
  }
  cout << score << endl;
  return 0;
}