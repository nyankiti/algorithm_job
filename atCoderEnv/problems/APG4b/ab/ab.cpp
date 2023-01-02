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

int read_int(map<string, int> &var_int) {
  string val;
  cin >> val;

  return isdigit(val.at(0))
             ? stoi(val)  // 数値の場合
             : var_int.at(
                   val);  // 変数の場合(過去に読み込まれた変数が存在することが保証されている)
}

int calc_int(map<string, int> &var_int) {
  string symbol = "";
  int result = 0;
  while (symbol != ";") {
    int val = read_int(var_int);

    // 記号が入力されてない場合（式の最初の項）は結果にそのまま代入
    if (symbol == "") {
      result = val;
    }
    // 足し算の場合
    if (symbol == "+") {
      result += val;
    }
    // 引き算の場合
    if (symbol == "-") {
      result -= val;
    }

    // symbolには"+", "-", ";"のいずれかが入力される
    cin >> symbol;
  }
  return result;
}

vector<int> read_vec_val(map<string, int> &var_int) {
  vector<int> result;  // 結果を保持する変数
  string symbol = "";  // vec値中の記号を受け取る変数

  // vec値の終わりである"]"が出てくるまで読み取る
  while (symbol != "]") {
    // 数値を1つ読み取ってvecに追加
    int val = read_int(var_int);
    result.push_back(val);

    // symbolには","か"]"が入力される
    cin >> symbol;
  }

  return result;
}

vector<int> read_vec(map<string, int> &var_int,
                     map<string, vector<int>> &var_vec) {
  string val;
  cin >> val;

  // "["かどうかでvec値か変数かを判定
  return val == "[" ? read_vec_val(var_int)  // vec値の場合
                    : var_vec.at(val);       // 変数の場合
}

vector<int> calc_vec(map<string, int> &var_int,
                     map<string, vector<int>> &var_vec) {
  string symbol;       // 演算子を受け取る変数
  vector<int> result;  // 結果を保持する変数

  // 式の終わりである";"が出てくるまで読み取る
  while (symbol != ";") {
    // 項を1つ読み取る
    vector<int> vec = read_vec(var_int, var_vec);

    // 記号が入力されてない場合（式の最初の項）は結果にそのまま代入
    if (symbol == "") {
      result = vec;
    }
    // 足し算の場合
    if (symbol == "+") {
      for (int i = 0; i < result.size(); i++) {
        result.at(i) += vec.at(i);
      }
    }
    // 引き算の場合
    if (symbol == "-") {
      for (int i = 0; i < result.size(); i++) {
        result.at(i) -= vec.at(i);
      }
    }

    // symbolには"+", "-", ";"のいずれかが入力される
    cin >> symbol;
  }

  return result;
}

void print_vec(vector<int> vec) {
  cout << "[ ";
  for (int i = 0; i < vec.size(); i++) {
    cout << vec.at(i) << " ";
  }
  cout << "]" << endl;
}

// 変数名を読み取りイコールを読み飛ばす
string read_name() {
  string name, equal;
  cin >> name >> equal;
  return name;
}

int main() {
  int N;
  cin >> N;

  map<string, int> var_int;
  map<string, vi> var_vec;

  rep(i, N) {
    string s;
    cin >> s;
    if (s == "int") {
      string name = read_name();
      var_int[name] = calc_int(var_int);
    }
    if (s == "vec") {
      string name = read_name();
      var_vec[name] = calc_vec(var_int, var_vec);
    }
    if (s == "print_int") {
      cout << calc_int(var_int) << endl;
    }
    if (s == "print_vec") {
      print_vec(calc_vec(var_int, var_vec));
    }
  }

  return 0;
}