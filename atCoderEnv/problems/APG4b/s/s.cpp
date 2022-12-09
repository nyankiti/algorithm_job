#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main()
{
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  rep(i, M)
  {
    cin >> A.at(i) >> B.at(i);
  }

  // char型の場合は、シングルコートを使う '-', string型の場合はダブルコートを使う " "
  // 縦がN, 横がvector<char>(N, '-') のans_tableを定義する
  vector<vector<char>> ans_table(N, vector<char>(N, '-'));
  rep(i, M)
  {
    A[i]--;
    B[i]--;
    ans_table[A.at(i)][B.at(i)] = 'o';
    ans_table[B.at(i)][A.at(i)] = 'x';
  }
  rep(i, N) rep(j, N)
  {
    cout << ans_table[i][j];
    if (j == N - 1)
    {
      cout << endl;
    }
    else
    {
      cout << " ";
    }
  }

  return 0;
}