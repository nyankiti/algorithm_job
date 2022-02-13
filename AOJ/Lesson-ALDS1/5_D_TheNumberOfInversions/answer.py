'''
参考記事：https://future-architect.github.io/articles/20210720a/
merge sortしながらinversionの数も数えられる
'''
from sys import stdin

n = int(stdin.readline())
*A, = map(int, stdin.readline().split())

count_inversion = 0


def merge_and_count(list_a, list_b):
    len_a = len(list_a)
    len_b = len(list_b)
    idx_a = 0
    idx_b = 0
    count_inversion = 0
    merged = []

    # リストの両方が空でないとき
    while idx_a < len_a and idx_b < len_b:
        if list_a[idx_a] < list_b[idx_b]:
            merged.append(list_a[idx_a])
            idx_a += 1
        else:
            merged.append(list_b[idx_b])
            idx_b += 1
            # count_inversionを、Aの残っている要素数の分だけ増やす
            count_inversion += len_a - idx_a

    # リストの一方が空になったら、他方のリストの残りを全て出力リストに加える
    if idx_a < len_a:
        merged += list_a[idx_a:]
    if idx_b < len_b:
        merged += list_b[idx_b:]

    return count_inversion, merged


def sort_and_count(lis):
    if len(lis) == 1:
        return 0, lis
    if len(lis) == 2:
        if lis[0] < lis[1]:
            return 0, lis
        else:
            return 1, [lis[1], lis[0]]
    else:
        # リストをほぼ2等分する
        half = len(lis) // 2
        list_first = lis[:half]
        list_second = lis[half:]
        inversion_first, sorted_first = sort_and_count(list_first)
        inversion_second, sorted_second = sort_and_count(list_second)
        inversion_while_merging, sorted_full = merge_and_count(
            sorted_first, sorted_second)

        return inversion_first + inversion_second + inversion_while_merging, sorted_full


print(sort_and_count(A)[0])
