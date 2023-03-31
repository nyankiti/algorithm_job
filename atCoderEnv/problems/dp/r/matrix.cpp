#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>; // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1 << 30) - 1)
#define LINF (1LL << 60)
// 非常に小さい値を表す epsilon。浮動小数展比較において、誤差の範囲を表すために使用する。10^(-10)を表している。
#define EPS (1e-10)

class SquareMatrix {
private:
    vector<vector<double>> data;
    size_t size;

public:
    // 大きさだけで初期化する場合
    explicit SquareMatrix(size_t N) : data(N, vector<double>(N)), size(N) {}
    // 行列で初期化する場合
    explicit SquareMatrix(const vector<vector<double>> &data) : size(data.size()), data(data) {}

    double get(int i, int j) { return data[i][j]; }
    void set(int i, int j, double val) { data[i][j] = val; }

    // 行列を表示
    void print() {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                cout << data[i][j] << " ";
            }
            cout << endl;
        }
    }

    // 行列の大きさを取得
    size_t getSize() {
        return size;
    }

    // 行列を転置する
    SquareMatrix transpose() {
        SquareMatrix newData(size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                // newData.set(i, j, data[j][i]);
                newData.data[i][j] = data[j][i];
            }
        }
        return newData;
    }

    // 行列同士の加算
    SquareMatrix operator+(SquareMatrix &other) {
        SquareMatrix newData(size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                newData.set(i, j, data[i][j] + other.get(i, j));
            }
        }
        return newData;
    }

    // 行列同士の減算
    SquareMatrix operator-(SquareMatrix &other) {
        SquareMatrix newData(size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                newData.set(i, j, data[i][j] - other.get(i, j));
            }
        }
        return newData;
    }

    // 行列の積
    SquareMatrix operator*(const SquareMatrix &other) {
        SquareMatrix newData(size);
        for (int i = 0; i < size; i++)
            for (int j = 0; j < size; j++) {
                double temp_sum = 0;
                for (int k = 0; k < size; k++) {
                    // dataが整数の場合
                    // newData.data[i][j] += this->data[i][k] * other.data[k][j] % MOD;
                    // newData.data[i][j] %= MOD;

                    // dataがdouble型の場合
                    temp_sum += this->data[i][k] * other.data[k][j];
                }
                newData.set(i, j, temp_sum);
            }
        return newData;
    }

    // 繰り返し二乗法で累乗を計算する
    SquareMatrix power(ll k) {
        if (k == 0) {
            // 単位行列を返す
            SquareMatrix I(size);
            for (int i = 0; i < size; i++)
                I.set(i, i, 1);
            return I;
        }
        SquareMatrix res = this->power(k / 2);
        res = res * res;
        if (k % 2 == 1) {
            SquareMatrix my_instance = *this;
            res = res * my_instance;
        }
        return res;
    }
    // 行列式を計算する
    double determinant() {
        if (size == 1) {
            return data[0][0];
        } else {
            double det = 0;
            for (int j = 0; j < size; j++) {
                SquareMatrix submatrix = getSubmatrix(0, j);
                double sign = pow(-1, j);
                det += sign * data[0][j] * submatrix.determinant();
            }
            return det;
        }
    }

    // 子行列を取得する(行列式の計算の際、余因子行列を取り出す時に使う)
    SquareMatrix getSubmatrix(int row, int col) {
        SquareMatrix submatrix(size - 1);
        int r = 0;
        for (int i = 0; i < size; i++) {
            if (i == row)
                continue;
            int c = 0;
            for (int j = 0; j < size; j++) {
                if (j == col)
                    continue;
                submatrix.set(r, c, get(i, j));
                c++;
            }
            r++;
        }
        return submatrix;
    }

    // 逆行列を計算する
    SquareMatrix inverse() {
        double det = this->determinant();
        if (det == 0) {
            // 行列式が0の場合は逆行列は存在しない
            throw std::runtime_error("matrix is not invertible");
        }

        // 随伴行列 adjugate
        SquareMatrix adjugate(size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                double sign = pow(-1, i + j);
                SquareMatrix submatrix = getSubmatrix(i, j);
                double cofactor = sign * submatrix.determinant();
                adjugate.set(j, i, cofactor);
            }
        }

        SquareMatrix inverse(size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                double value = adjugate.get(i, j) / det;
                inverse.set(i, j, value);
            }
        }
        return inverse;
    }
};

int main() {
    SquareMatrix A(2), B(2);
    A.set(0, 0, 1);
    A.set(0, 1, 2);
    A.set(1, 0, 3);
    A.set(1, 1, 4);

    B.set(0, 0, 5);
    B.set(0, 1, 6);
    B.set(1, 0, 7);
    B.set(1, 1, 8);

    cout << "matrix A" << endl;
    A.print();
    cout << "matrix B" << endl;
    B.print();
    cout << "A + B" << endl;
    SquareMatrix C = A + B;
    C.print();
    cout << "A - B" << endl;
    SquareMatrix D = A - B;
    D.print();
    cout << "A * B" << endl;
    SquareMatrix E = A * B;
    E.print();

    cout << "transposen of A" << endl;
    SquareMatrix F = A.transpose();
    F.print();

    SquareMatrix G(4);
    G.set(0, 0, 1);
    G.set(0, 1, 7);
    G.set(0, 2, 2);
    G.set(0, 3, 4);
    G.set(1, 0, 1);
    G.set(1, 1, 5);
    G.set(1, 2, 2);
    G.set(1, 3, 4);
    G.set(2, 0, 3);
    G.set(2, 1, 0);
    G.set(2, 2, 1);
    G.set(2, 3, 0);
    G.set(3, 0, 2);
    G.set(3, 1, 1);
    G.set(3, 2, 5);
    G.set(3, 3, -3);
    cout << "matrix G" << endl;
    G.print();

    cout << "determinant of G" << endl;
    cout << G.determinant() << endl;

    SquareMatrix H(3);
    H.set(0, 0, 1);
    H.set(0, 1, 1);
    H.set(0, 2, -1);
    H.set(1, 0, -2);
    H.set(1, 1, 0);
    H.set(1, 2, 1);
    H.set(2, 0, 0);
    H.set(2, 1, 2);
    H.set(2, 2, 1);
    SquareMatrix H_inversed = H.inverse();
    cout << "matrix H" << endl;
    H.print();
    cout << "H inversed" << endl;
    H_inversed.print();
    return 0;
}