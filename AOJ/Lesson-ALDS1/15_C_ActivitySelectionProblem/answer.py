'''
活動(アクティビティ)選択問題
貪欲法で解ける組み合わせ最適化問題の一つ
終了時刻で並び替えて、可能なアクティビティを全て参加するという貪欲法で解ける


アクティビティ選択問題は、間隔スケジューリング最大化問題（ISMP）とも呼ばれ、
より一般的な間隔スケジューリング問題の特殊なタイプです
'''
from sys import stdin

n = int(stdin.readline())

# (start_time, end_time) というtupleを配列に格納する
activities = []

for _ in range(n):
    s, t = map(int, stdin.readline().split())
    activities.append((s, t))

# 活動を終了時刻の小さい順に並び替え
activities.sort(key=lambda x: x[1])

count = 0
max_t = 0  # 参加を決めた活動のうち、最も遅く終わるものの終了時刻をもっておく

for s, t in activities:
    if s > max_t:
        count += 1
        max_t = t

print(count)
