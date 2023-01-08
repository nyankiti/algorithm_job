from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    K = int(stdin.readline())
    meeting_time = []
    for _ in range(N):
        l, r = map(int, stdin.readline().split())
        # 全ての会議の終了時刻を K 秒遅らせておくことで、会議の後に開けるべき間隔を考慮する
        meeting_time.append([l, r+K])

    # 終了時間でソートする
    meeting_time.sort(key=lambda x: x[1])

    # 時刻 i までに最大で幾つの会議に出席できるかを記録した配列 countL
    countL = [0]*200001

    meeting_idx = 0
    current_time = 0
    for i in range(1, 200001):
        if meeting_idx < len(meeting_time) and meeting_time[meeting_idx][1] == i:
            if current_time <= meeting_time[meeting_idx][0]:
                countL[i] = countL[i-1]+1
                current_time = meeting_time[meeting_idx][1]
            else:
                countL[i] = countL[i-1]
            meeting_idx += 1
        else:
            countL[i] = countL[i-1]

    # 時刻 i 以降で最大で幾つの会議に出席できるかを記録した配列 countR
    countR = [0]*200001

    # 開始時間でソートする
    # for i in range(N):
    #     meeting_time[i] = [meeting_time[i][0]-K, meeting_time[i][1]-K]
    meeting_time.sort(key=lambda x: x[0])

    meeting_idx = len(meeting_time)-1
    current_time = float("inf")
    for i in range(199999, 0, -1):
        if meeting_idx >= 0 and meeting_time[meeting_idx][0] == i:
            if current_time >= meeting_time[meeting_idx][1]:
                countR[i] = countR[i+1]+1
                current_time = meeting_time[meeting_idx][0]
            else:
                countR[i] = countR[i+1]
            meeting_idx -= 1
        else:
            countR[i] = countR[i+1]

    for i in range(N):
        l, r = meeting_time[i]
        print(countL[l] + 1 + countR[r])


if __name__ == '__main__':
    main()
