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

class Rectangle {
 public:
  Rectangle() : height_(0), width_(0) {
    cout << "デフォルトコンストラクタ" << endl;
  }
  Rectangle(int height, int width) : height_(height), width_(width) {
    cout << "引数ありコンストラクタ" << endl;
  }
  // コピーコンストラクタは参照渡し
  Rectangle(const Rectangle& r) : height_(r.height_), width_(r.width_) {
    cout << "コピーコンストラクタ" << endl;
  }

  int Area() const { return height_ * width_; }

 private:
  const int height_;
  const int width_;
};

class Square {
 public:
  explicit Square(int size) : size_(size) {}
  // Square(int size) : size_(size) {}

  Square() = default;

  int Area() const { return size_ * size_; }

 private:
  int size_;
};

int main() {
  // デフォルトコンストラクタ
  Rectangle r1;

  // 引数付きコンストラクタ(r2, r3, r4)
  Rectangle r2(2, 3);
  /*
   C++11 で導入されたUniversal Initialization(一様初期化構文)
  (https://cpprefjp.github.io/lang/cpp11/uniform_initialization.html)
   によって、以下の二つのような呼び出し方もできる。
  */
  Rectangle r3 = {2, 3};
  Rectangle r4{2, 3};

  // コピーコンストラクタ
  Rectangle r5 = r4;

  /*
  explictを使うと、= を用いた暗黙的なコンストラクタの呼び出しができなくなる。
  一つした引数を受け取らないコンストラクタの宣言を統一するために
  explicitを使う。
  */
  Square s1(2);
  // コンストラクタに explicit 修飾子をつけると、以下の宣言はエラーになる。
  // Square s2 = 2;

  /*
  defaultによってデフォルトコンストラクタが動作するように指定しているので、以下のように初期化できる
  ただし、初期値は変な値になっている(バグらないだけで、このような宣言はお勧めしない)
  */
  Square s3;
  cout << s3.Area() << endl;

  return 0;
}