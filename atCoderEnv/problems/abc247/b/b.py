from sys import stdin, exit


def main():
    def judge():
        def judge2(u, idx):
            # 人idxがuをあだ名に使えるか？
            for i in range(N):
                if i == idx:
                    continue  # 自分自身の姓名とは被ってもいいです
                if u in ST[i]:  # u == s or u == tと同じです
                    return False
            return True

        N = int(input())
        ST = [input().split() for _ in range(N)]
        for i in range(N):
            si, ti = ST[i]
            if not (judge2(si, i) or judge2(ti, i)):
                return False  # siもtiもあだ名にできなければ、人iにあだ名をつけられないので`No`です
        return True  # 全員にあだ名をつけられたので、`Yes`です

    print("Yes" if judge() else "No")


if __name__ == '__main__':
    main()
