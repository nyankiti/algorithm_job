#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int count_report_sum(vector<vector<int>> &children, int x)
{
  // base case (下部組織を持たない組織はすぐに報告を送れる)
  if (children[x].size() == 0)
  {
    return 1;
  }
  int sum = 0;
  for (int child : children[x])
  {
    sum += count_report_sum(children, child);
  }
  return sum + 1;
}

int main()
{
  int N;
  cin >> N;
  vector<int> P(N);
  P[0] = -1;
  for (int i = 1; i < N; i++)
  {
    cin >> P[i];
  }

  // それぞれの組織が持つ下部組織をvectorで管理する
  vector<vector<int>> children(N);
  for (int i = 1; i < N; i++)
  {
    int parent = P[i];
    children[parent].push_back(i);
  }

  for (int i = 0; i < N; i++)
  {
    cout << count_report_sum(children, i) << endl;
  }

  return 0;
}