#include <bits/stdc++.h>
using namespace std;

set<long long> Set1, Set2;

long long GetDown(long long r)
{
  auto itr = Set2.lower_bound(-r);
  if (itr == Set2.end())
    return -1000000000000LL;
  return -(*itr);
}

long long GetUp(long long r)
{
  auto itr = Set1.lower_bound(r);
  if (itr == Set1.end())
    return 1000000000000LL;
  return (*itr);
}

int main()
{
  int Q, QueryType[100009], x[100009];
  cin >> Q;
  for (int i = 1; i <= Q; i++)
    cin >> QueryType[i] >> x[i];

  for (int i = 1; i <= Q; i++)
  {
    if (QueryType[i] == 1)
    {
      Set1.insert(x[i]);
      Set2.insert(-x[i]);
    }
    if (QueryType[i] == 2)
    {
      long long v1 = GetDown(x[i]);
      long long v2 = GetUp(x[i]);
      long long Answer = min(x[i] - v1, v2 - x[i]);
      if (Answer >= 100000000000LL)
        cout << -1 << endl;
      else
        cout << Answer << endl;
    }
  }
  return 0;
}