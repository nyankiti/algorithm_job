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
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

class UnionFind {
public:
    explicit UnionFind(size_t n) : parents(n, -1) {}

    // 頂点 i のrootのインデックスを返す
    int find(int i) {
        if (parents[i] < 0) {
            return i;
        }
        parents[i] = find(parents[i]);
        return parents[i];
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            // union by size(小さい方を子にしてメモリを削減)
            if (parents[a] < parents[b])
                swap(a, b);
            parents[a] += parents[b];
            parents[b] = a;
        }
    }

    bool is_same(int a, int b) { return (find(a) == find(b)); }

    int size(int i) { return -parents[find(i)]; }

private:
    vector<int> parents;
};

int N, M;
vi graph[200009];
bool visited[200009];
map<int, int> edge_cnt_map;

int dfs(int v) {
    visited[v] = true;
    int vertex_count = edge_cnt_map[v];
    for (int adj : graph[v]) {
        if (visited[adj] == false) {
            vertex_count += dfs(adj);
        }
    }
    return vertex_count;
}

bool solve() {
    cin >> N >> M;
    UnionFind uf = UnionFind(N);
    rep(i, 0, M) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
        edge_cnt_map[u] += 1;
        uf.unite(u, v);
    }
    rep(i, 0, N) visited[i] = false;
    // dfsによって連結成分の辺の数を数える
    rep(i, 0, N) {
        if (visited[i] == false) {
            if (uf.size(i) != dfs(i)) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    cout << (solve() ? "Yes" : "No") << endl;
    return 0;
}