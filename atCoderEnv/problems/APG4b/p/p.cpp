#include <bits/stdc++.h>
using namespace std;

int sum(vector<int> scores)
{
  int score_sum = 0;
  for (int i : scores)
  {
    score_sum += i;
  }
  return score_sum;
}

void output(int sum_a, int sum_b, int sum_c)
{
  // ここにプログラムを追記
  cout << sum_a * sum_b * sum_c << endl;
}

// N個の入力を受け取って配列に入れて返す関数
// 引数 N: 入力を受け取る個数
// 返り値: 受け取ったN個の入力の配列
vector<int> input(int N)
{
  vector<int> vec(N);
  for (int i = 0; i < N; i++)
  {
    cin >> vec.at(i);
  }
  return vec;
}

int main()
{
  // 科目の数Nを受け取る
  int N;
  cin >> N;

  // それぞれのテストの点数を受け取る
  vector<int> A = input(N);
  vector<int> B = input(N);
  vector<int> C = input(N);

  // それぞれの合計点を計算
  int sum_A = sum(A);
  int sum_B = sum(B);
  int sum_C = sum(C);

  // プレゼントの予算を出力
  output(sum_A, sum_B, sum_C);

  return 0;
}