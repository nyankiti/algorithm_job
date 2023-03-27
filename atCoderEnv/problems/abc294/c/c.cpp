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

int N, M, A[100009], B[100009];
int main() {
    cin >> N >> M;
    for (int i = 1; i <= N; i++)
        cin >> A[i];
    for (int i = 1; i <= M; i++)
        cin >> B[i];

    int a_idx = 1, b_idx = 1, i = 1;
    while (i <= M + N) {
        if (a_idx > N) {
            B[b_idx] = i;
            b_idx++;
        } else if (b_idx > M) {
            A[a_idx] = i;
            a_idx++;
        } else if (A[a_idx] < B[b_idx]) {
            A[a_idx] = i;
            a_idx++;
        } else {
            B[b_idx] = i;
            b_idx++;
        }
        i++;
    }
    for (int i = 1; i <= N; i++)
        cout << A[i] << " ";
    cout << endl;
    for (int i = 1; i <= M; i++)
        cout << B[i] << " ";
    cout << endl;
    return 0;
}