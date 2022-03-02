from sys import stdin

n = int(stdin.readline())
cards = []

# 安定を判別するためのdict
# 出現する数ごとに、H, S, C, D の絵柄の順番が変化していなければ良いので、入力受け取り時にその順番を、各数ごとに記録しておく
num_idx = {} #各数の出現回数を数えるdict
num_list = {} #各数の絵柄を出現順に記録するためのdict

for _ in range(n):
    suit, num  = stdin.readline().split()
    num = int(num)
    cards.append((suit, num))
    if num not in num_idx:
        num_idx[num] = 0
        num_list[num] = []
    
    num_list[num].append(suit)


def partition(A, p, r):
    pivot = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
                
    A[i+1], A[r] = A[r], A[i+1]
    return i+1



def quick_sort(cards):
    def _quick_sort(cards, start, end):
        if start < end:
            partition_index = partition(cards, start, end)
            _quick_sort(cards, partition_index+1, end)
            _quick_sort(cards, start, partition_index-1)
    _quick_sort(cards, 0, len(cards)-1)

quick_sort(cards)


is_stable = True

for suit, num in cards:
    if num_list[num][num_idx[num]] != suit:
        is_stable = False
        break
    num_idx[num] += 1

print('Stable' if is_stable else 'Not stable')
for card in cards:
    print(*card)