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

int N, Q, X;
int A[100009];

int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  sort(begin(A) + 1, begin(A) + N + 1);
  cin >> Q;
  rep(i, 0, Q) {
    cin >> X;
    auto it = lower_bound(begin(A) + 1, begin(A) + N + 1, X);
    // イテレータはメモリ上に、隙間なく並んでいる領域を指したポインターであるので、最初の位置を引くことで配列の相対的なindexを取得できる
    int index = it - begin(A);
    // 値を取りたい場合は、直接ポインターの値を読み込めば良い *it とするだけ。
    cout << index - 1 << endl;
  }
  return 0;
}