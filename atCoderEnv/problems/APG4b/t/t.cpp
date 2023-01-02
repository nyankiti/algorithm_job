#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)

// 参照渡しの場合は変数の頭に & をつける
void saiten(vector<vector<int>> &A, int &correct_count, int &wrong_count)
{
  rep(i, 9) rep(j, 9)
  {
    if (A[i][j] == (i + 1) * (j + 1))
    {
      correct_count++;
    }
    else
    {
      wrong_count++;
      A[i][j] = (i + 1) * (j + 1);
    }
  }
}

int main()
{
  vector<vector<int>> A(9, vector<int>(9));
  rep(i, 9) rep(j, 9)
  {
    cin >> A[i][j];
  }
  int correct_count = 0; // ここに正しい値のマスの個数を入れる
  int wrong_count = 0;   // ここに誤った値のマスの個数を入れる

  // A, correct_count, wrong_countを参照渡し
  saiten(A, correct_count, wrong_count);

  // 正しく修正した表を出力
  for (int i = 0; i < 9; i++)
  {
    for (int j = 0; j < 9; j++)
    {
      cout << A.at(i).at(j);
      if (j < 8)
        cout << " ";
      else
        cout << endl;
    }
  }
  // 正しいマスの個数を出力
  cout << correct_count << endl;
  // 誤っているマスの個数を出力
  cout << wrong_count << endl;

  return 0;
}