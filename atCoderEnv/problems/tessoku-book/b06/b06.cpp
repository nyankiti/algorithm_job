#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using pii = pair<int, int>;
/* macro */
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep_a(i, a, n) for (int i = (a); i < (n); ++i)

int main() {
  int N, Q, L, R, A[100009], atari[100009], hazure[100009];
  cin >> N;
  rep_a(i, 1, N + 1) { cin >> A[i]; }
  atari[0] = 0;
  hazure[0] = 0;
  rep_a(i, 1, N + 1) {
    atari[i] = atari[i - 1];
    hazure[i] = hazure[i - 1];
    if (A[i] == 1) {
      atari[i]++;
    } else {
      hazure[i]++;
    }
  }
  int atari_count, hazure_count;
  cin >> Q;
  rep(i, Q) {
    cin >> L >> R;
    atari_count = atari[R] - atari[L - 1];
    hazure_count = hazure[R] - hazure[L - 1];
    string ans;
    if (atari_count == hazure_count) {
      ans = "draw";
    } else if (atari_count > hazure_count) {
      ans = "win";
    } else {
      ans = "lose";
    }
    cout << ans << endl;
  }

  return 0;
}