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

void compress(vi& A) {
  set<int> A_set;
  map<int, int> compress_mapping;
  for (int v : A) A_set.insert(v);
  int compressed_val = 1;
  for (auto v : A_set) {
    compress_mapping[v] = compressed_val;
    compressed_val += 1;
  }
  rep(i, 0, A.size()) { A[i] = compress_mapping[A[i]]; }
}

int H, W, N;
int main() {
  cin >> H >> W >> N;
  vi row;
  vi col;
  rep(i, 0, N) {
    int a, b;
    cin >> a >> b;
    row.push_back(a);
    col.push_back(b);
  }
  compress(row);
  compress(col);
  rep(i, 0, N) { cout << row[i] << " " << col[i] << endl; }
  return 0;
}