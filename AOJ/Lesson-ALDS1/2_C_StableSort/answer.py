N = int(input())
li = input().split()


def check_lists_stable(original_li, sorted_li):
    for i in range(1, 13):
        original_result = []
        sorted_result = []
        # 番号ごとにまとめて、その順番が一致するかどうかでstableを判定する
        for j in range(len(original_li)):
            if int(original_li[j][1:]) == i:
                original_result.append(original_li[j])
            if int(sorted_li[j][1:]) == i:
                sorted_result.append(sorted_li[j])
        if original_result != sorted_result:
            return False
    return True


# bubble sort
bubble_li = li[:]
bubble_is_stable = True
for i in range(N):
    for j in range(0, N-i-1):
        if bubble_li[j][1:] > bubble_li[j+1][1:]:
            bubble_li[j], bubble_li[j+1] = bubble_li[j+1], bubble_li[j]
print(*bubble_li)
if check_lists_stable(li, bubble_li):
    print("Stable")
else:
    print("Not stable")

# selection sort
selection_li = li[:]
for i in range(N):
    min_index = i
    for j in range(i, N):
        if selection_li[j][1:] < selection_li[min_index][1:]:
            min_index = j
    selection_li[i], selection_li[min_index] = selection_li[min_index], selection_li[i]

print(*selection_li)
if check_lists_stable(li, selection_li):
    print("Stable")
else:
    print("Not stable")


'''
bubble sortはstableであるが、selection sortはstableではない。
この問題は、この性質を利用することで、
selection sort の結果がbubble sortの結果と一致すると、stableであると判断できる。
'''
