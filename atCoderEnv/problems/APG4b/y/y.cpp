#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main()
{
  int N;
  cin >> N;
  vector<int> A(N);
  rep(i, N)
  {
    cin >> A.at(i);
  }

  map<int, int> cnt;
  for (int a : A)
  {
    if (cnt.count(a))
    {
      cnt.at(a)++;
    }
    else
    {
      cnt[a] = 1;
    }
  }

  int max_cnt = 0;
  int ans = -1;
  for (int a : A)
  {
    if (max_cnt < cnt.at(a))
    {
      max_cnt = cnt.at(a);
      ans = a;
    }
  }

  cout << ans << " " << max_cnt << endl;

  return 0;
}