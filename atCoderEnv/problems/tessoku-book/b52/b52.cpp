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

int N, X;
string A;
int main() {
  cin >> N >> X >> A;
  deque<int> deq;
  deq.push_back(X - 1);
  A[X - 1] = '@';
  while (!deq.empty()) {
    int pos = deq.front();
    if (pos - 1 >= 0 && A[pos - 1] == '.') {
      A[pos - 1] = '@';
      deq.push_back(pos - 1);
    }
    if (pos + 1 < A.size() && A[pos + 1] == '.') {
      A[pos + 1] = '@';
      deq.push_back(pos + 1);
    }
    deq.pop_front();
  }
  cout << A << endl;
  return 0;
}