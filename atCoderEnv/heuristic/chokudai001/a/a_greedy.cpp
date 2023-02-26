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

// プレイヤーの座標を保持する struct
struct Coord {
    int x_;
    int y_;
    Coord(const int x = 0, const int y = 0) : x_(x), y_(y) {}
};

mt19937 mt_for_action(/* 行動選択用のseed */ 0); // 行動選択用の乱数生成器を初期化

class GameState {
private:
    // 0 => 右, 1 => 左 , 2 => 下 , 3 => 上 としてactionを扱う
    static constexpr const int dx[4] = {1, -1, 0, 0};
    static constexpr const int dy[4] = {0, 0, 1, -1};

public:
    // 点数を表すvector
    vector<vector<int>> points_;
    Coord character_ = Coord();
    int evaluated_score_ = 0; // 探索上で評価したスコア
    int first_action_ = -1;   // ビームサーチ用の最初に選択した行動
    // コンストラクにて初期盤面の反映
    GameState() {}
    GameState(const vector<vector<int>> &A) {
        points_ = A;
    }
    // [どのゲームでも実装する] : ゲームの終了判定
    bool isDone() const {
        bool isGameDone = true;
        rep(i, 0, 30) {
            rep(j, 0, 30) {
                if (this->points_[i][j] != 0) {
                    isGameDone = false;
                    break;
                }
            }
        }
        return isGameDone;
    }

    // [どのゲームでも実装する] : 探索用の盤面評価をする
    void evaluateScore() {
        auto legal_actions = this->legalActions();
        this->evaluated_score_ = legal_actions.size(); // 横に進める数が多い場合に盤面の評価を高くする
    }

    // [どのゲームでも実装する] : 指定したactionでゲームを1ターン進める
    void advance(const int action) {
        this->character_.x_ += dx[action];
        this->character_.y_ += dy[action];
        auto &point = this->points_[this->character_.x_][this->character_.y_];
        if (point > 0) {
            // 高橋君が数を減らすマス出力する
            cout << this->character_.x_ + 1 << " " << this->character_.y_ + 1 << endl;
            // 値を1減らす
            point -= 1;
        }
    }

    // 現在キャラクターがいるマスから可能な行動を全て返す
    vector<int> legalActions() const {
        vector<int> actions;
        for (int action = 0; action < 4; action++) {
            int ty = this->character_.y_ + dy[action];
            int tx = this->character_.x_ + dx[action];
            if (ty >= 0 && ty < 30 && tx >= 0 && tx < 30 && this->points_[tx][ty] != 0) {
                // 選んでいるマスと同じ数字の場合は進める
                if (this->points_[this->character_.x_][this->character_.y_] == this->points_[tx][ty]) {
                    actions.emplace_back(action);
                }
            }
        }
        return actions;
    }

    string toString() const {
        stringstream ss;
        rep(i, 0, 30) {
            rep(j, 0, 30) { ss << this->points_[i][j] << " "; }
            ss << endl;
        }
        return ss.str();
    }
};

// [どのゲームでも実装する] : 探索時のソート用に評価を比較する
bool operator<(const GameState &maze_1, const GameState &maze_2) {
    return maze_1.evaluated_score_ < maze_2.evaluated_score_;
}

int main() {
    vector<vector<int>> A(30, vector<int>(30));
    rep(i, 0, 30) rep(j, 0, 30) cin >> A[i][j];

    auto gameState = GameState(A);

    // 大きい数字がある座標から順番にチェックしていく
    while (!gameState.isDone()) {
        int max_point = 0, x = 0, y = 0;
        rep(i, 0, 30) rep(j, 0, 30) {
            if (gameState.points_[i][j] > max_point) {
                max_point = gameState.points_[i][j];
                x = i;
                y = j;
            }
        }
        // (x, y) にキャラクターを配置し、指定の操作(問題における「手」)を行う「
        auto &point = gameState.points_[x][y];
        if (point == 0)
            continue;
        else {
            gameState.character_ = Coord(x, y);
            // 高橋君が数を減らすマス出力する
            cout << gameState.character_.x_ + 1 << " " << gameState.character_.y_ + 1 << endl;
            point -= 1;
            // ランダムに移動する場合
            while (true) {
                auto legal_actions = gameState.legalActions();
                if (legal_actions.size() == 0) {
                    break;
                } else {
                    // 可能なactionのうちランダムで一つを選択する
                    gameState.advance(legal_actions[mt_for_action() % (legal_actions.size())]);
                }
            }
        }
    }
    cout << gameState.toString() << endl;

    return 0;
}