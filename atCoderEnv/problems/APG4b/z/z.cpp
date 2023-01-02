#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using pii = pair<int, int>;
/* macro */
#define rep(i, n) for (int i = 0; i < (n); ++i)

struct Clock
{
  int hour;
  int minute;
  int second;

  void set(int h, int m, int s)
  {
    hour = h;
    minute = m;
    second = s;
  }

  string to_str()
  {
    string ret;

    if (hour < 10)
      ret += "0";
    ret += to_string(hour);
    ret += ":";

    if (minute < 10)
      ret += "0";
    ret += to_string(minute);
    ret += ":";

    if (second < 10)
      ret += "0";
    ret += to_string(second);

    return ret;
  }
  void shift(int diff_second)
  {
    int diff_hour = diff_second / 3600;
    diff_second %= 3600;
    int diff_minute = diff_second / 60;
    diff_second %= 60;

    second += diff_second;
    if (second >= 60)
    {
      // 分へ繰り上げ
      minute += 1;
      second -= 60;
    }
    else if (second < 0)
    {
      // 分から繰り下げ
      minute -= 1;
      second += 60;
    }

    minute += diff_minute;
    if (minute >= 60)
    {
      // 時へ繰り上げ
      hour += 1;
      minute -= 60;
    }
    else if (minute < 0)
    {
      // 時から繰り下げ
      hour -= 1;
      minute += 60;
    }

    hour += diff_hour;
    if (hour >= 24)
    {
      hour -= 24;
    }
    else if (hour < 0)
    {
      hour += 24;
    }
  }
};

int main()
{
  // 入力を受け取る
  int hour, minute, second;
  cin >> hour >> minute >> second;
  int diff_second;
  cin >> diff_second;

  // Clock構造体のオブジェクトを宣言
  Clock clock;

  // set関数を呼び出して時刻を設定する
  clock.set(hour, minute, second);

  // 時刻を出力
  cout << clock.to_str() << endl;

  // 時計を進める(戻す)
  clock.shift(diff_second);

  // 変更後の時刻を出力
  cout << clock.to_str() << endl;

  return 0;
}