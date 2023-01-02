#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
// alias
using pii = pair<int, int>;
// macro
#define rep(i, n) for (int i = 0; i < (n); ++i)
int main()
{
  int N;
  cin >> N;
  vector<pii> p(N);
  rep(i, N)
  {
    int a, b;
    cin >> a >> b;
    p[i] = make_pair(b, a);
  }

  sort(p.begin(), p.end());

  rep(i, N)
  {
    int b, a;
    tie(b, a) = p[i];
    cout << a << " " << b << endl;
  }

  return 0;
}