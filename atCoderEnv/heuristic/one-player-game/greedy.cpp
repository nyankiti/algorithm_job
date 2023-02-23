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

// プライヤーの座標を保持する struct
struct Coord {
    int x_;
    int y_;
    Coord(const int x = 0, const int y = 0) : x_(x), y_(y) {}
};

using ScoreType = int64_t;                    // ゲームの評価スコアの型を決めておく。
constexpr const ScoreType INF = 1000000000LL; // あり得ないぐらい大きなスコアの例を用意しておく

class MazeState {
private:
    static constexpr const int dx[4] = {1, -1, 0, 0};
    static constexpr const int dy[4] = {0, 0, 1, -1};

    vector<vector<int>> points_;
    int turn_ = 0;
    int H_;
    int W_;
    int END_TURN_;

public:
    Coord character_ = Coord();
    int game_score_ = 0;
    ScoreType evaluated_score_ = 0; // 探索上で評価したスコア

    // コンストラクタ(迷路の初期盤面生成)
    MazeState(int seed, int H, int W, int END_TURN) : H_(H),
                                                      W_(W),
                                                      END_TURN_(END_TURN),
                                                      points_(H, vector<int>(W, 0)) {
        auto mt_for_construct = mt19937(seed); // 盤面構築用の乱数生成器を初期化
        // プレイヤーの位置を初期化
        this->character_.x_ = mt_for_construct() % H;
        this->character_.y_ = mt_for_construct() % W;
        rep(y, 0, H) {
            rep(x, 0, W) {
                if (x == this->character_.x_ && y == this->character_.y_) {
                    continue;
                }
                this->points_[y][x] = mt_for_construct() % 10;
            }
        }
    }

    // [どのゲームでも実装する] : ゲームの終了判定
    bool isDone() const { return this->turn_ == this->END_TURN_; }

    // [どのゲームでも実装する] : 探索用の盤面評価をする
    void evaluateScore() {
        this->evaluated_score_ = this->game_score_; // 簡単のため、まずはゲームスコアをそのまま盤面の評価とする
    }

    // [どのゲームでも実装する] : 指定したactionでゲームを1ターン進める
    void advance(const int action /* 0, 1, 2, 3 のうち、どれが入る */) {
        this->character_.x_ += dx[action];
        this->character_.y_ += dy[action];
        auto &point = this->points_[this->character_.y_][this->character_.x_];
        if (point > 0) {
            this->game_score_ += point;
            // 参照から実態の値を変更する
            point = 0;
        }
        this->turn_++;
    }

    // [どのゲームでも実装する] :
    // 現在の状況でプレイヤーが可能な行動を全て取得する
    vector<int> legalActions() const {
        vector<int> actions;
        for (int action = 0; action < 4; action++) {
            int ty = this->character_.y_ + dy[action];
            int tx = this->character_.x_ + dx[action];
            if (ty >= 0 && ty < this->H_ && tx >= 0 && tx < this->W_) {
                // push_backよりemplace_backの方が早い
                actions.emplace_back(action);
            }
        }
        return actions;
    }

    // [実装しなくてもよいが実装すると便利] : 現在のゲーム状況を文字列にする
    string toString() const {
        stringstream ss;
        ss << "turn:\t" << this->turn_ << "\n";
        ss << "score:\t" << this->game_score_ << "\n";
        for (int h = 0; h < this->H_; h++) {
            for (int w = 0; w < this->W_; w++) {
                if (this->character_.y_ == h && this->character_.x_ == w) {
                    ss << '@';
                } else if (this->points_[h][w] > 0) {
                    ss << points_[h][w];
                } else {
                    ss << '.';
                }
            }
            ss << '\n';
        }

        return ss.str();
    }
};

// 貪欲法で行動を決定する
int greedyAction(const MazeState &state) {
    auto legal_actions = state.legalActions();
    ScoreType best_score = -INF; // 絶対にありえない小さな値でベストスコアを初期化する
    int best_action = -1;        // ありえない行動で初期化する
    for (const auto action : legal_actions) {
        MazeState now_state = state;
        now_state.advance(action);
        now_state.evaluateScore();
        if (now_state.evaluated_score_ > best_score) {
            best_score = now_state.evaluated_score_;
            best_action = action;
        }
    }
    // 不安ならここに assert(best_score != -1); とチェックしても良い
    return best_action;
}

// 引数として、迷路の高さ H , 迷路の幅 W , ゲーム終了ターン END_TURN の順番に入っている
int main(int argc, char *argv[]) {
    // argv[0]はプログラム名やnullが入っており、通常は利用しない。
    int H = atoi(argv[1]),
        W = atoi(argv[2]),
        END_TURN = atoi(argv[3]),
        seed = atoi(argv[4]);

    // ゲームをプレイする
    auto state = MazeState(seed, H, W, END_TURN);
    cout << state.toString() << endl;
    while (!state.isDone()) {
        state.advance(greedyAction(state));
        cout << state.toString() << endl;
    }
    return 0;
}