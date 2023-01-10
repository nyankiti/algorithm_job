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

vector<ll> enumerate(vector<ll> A) {
  vector<ll> sum_list;
  // bit全探索でありえる組み合わせを列挙
  rep(i, 0, (1 << A.size())) {
    ll sum = 0;
    rep(j, 0, A.size()) {
      int wari = (1 << j);
      if ((i / wari) % 2 == 1) sum += A[j];
    }
    sum_list.push_back(sum);
  }
  return sum_list;
}

int main() {
  ll N, K, A[39];
  vector<ll> first_cards, second_cards;
  bool ans = false;

  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, N / 2 + 1) first_cards.push_back(A[i]);
  rep(i, N / 2 + 1, N + 1) second_cards.push_back(A[i]);

  // for (ll val : first_cards) cout << val << " ";
  // cout << endl;
  // for (ll val : second_cards) cout << val << " ";
  // cout << endl;

  vector<ll> first_sums = enumerate(first_cards);
  vector<ll> second_sums = enumerate(second_cards);
  sort(first_sums.begin(), first_sums.end());
  sort(second_sums.begin(), second_sums.end());

  // for (ll val : first_sums) cout << val << " ";
  // cout << endl;
  // for (ll val : second_sums) cout << val << " ";
  // cout << endl;

  for (auto i : first_sums) {
    ll target = K - i;
    auto it = lower_bound(second_sums.begin(), second_sums.end(), target);
    if (*it == target) ans = true;
  }

  cout << (ans ? "Yes" : "No") << endl;
  return 0;
}