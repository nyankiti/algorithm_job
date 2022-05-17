#include <bits/stdc++.h>
using namespace std;

int main()
{
  int a, digit, ans = 0;

  cin >> a;

  for (int i = 0; i < 3; i++)
  {
    digit = a % 10;
    if (digit == 1)
    {
      ans++;
    }
    a /= 10;
  }
  cout << ans << endl;
  return 0;
}