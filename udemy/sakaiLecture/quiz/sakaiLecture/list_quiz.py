# -------------------------------------------------------------------
'''
リストを使った足し算
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[8, 9] => [9, 0] => 90
[9, 9] => [1, 0, 0] => 100
[1, 2, 3] => [1, 2, 4] => 124
[7, 8, 9] => [7, 9, 0] => 790
[9, 9, 9] => [1, 0, 0, 0] => 1000
[9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
[0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
'''
# -------------------------------------------------------------------

# 一度文字列にして、それをjoinで連結してからintにもどし、最後に1を足すと簡単にできるが販促とする 
# l = [1, 2, 3]
# print(int(''.join([str(i) for i in l])) + 1)

from typing import List
import operator

def list_to_int_plus_one_by_me(numbers: List[int]) -> int:
  len_numbers = len(numbers)
  i = len_numbers - 1
  digit = 1
  answer = 0
  while i >= 0:
    temp_num = numbers[i]*digit
    answer += temp_num
    digit = digit*10
    i -= 1 

  return answer + 1

# --------------------------------------------------

def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10**i)
    return sum_numbers


def list_to_int_plus_one(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        numbers[i] = 0
        numbers[i-1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)



# -----------------------------------------------------------------
# スネーク表示問題-------------------------------------------------
# -----------------------------------------------------------------
def snake_stirng_v1(chars: str) -> List[List[int]]:
    result = [[], [], []]
    # 集合setで管理するとやりやすい
    result_indexes = {0, 1, 2}
    insert_index = 1
    # str型もindexで管理できる    str    abcde
    #                            index   01234
    # enumerate関数で文字列とインデックスを一緒に取り出す
    for i, s, in enumerate(chars):
        if i % 4 ==  1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)

        # 集合setの性質を用いて、'result_indexes - {insert_index}'  としてinsert_index以外のindexを取得(result_indexesは集合として定義しているので{}で囲む必要がない)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')
    return result




def snake_stirng_v2_by_me(chars: str, depth: int) -> List[List[int]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    for i, s, in enumerate(chars):
        for j in range(depth*2):
            if i % (depth*2) ==  j:
                insert_index = (int(depth / 2) + j) % 4

        result[insert_index].append(s)

    for rest_index in result_indexes - {insert_index}:
        result[rest_index].append(' ')
    return result


def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    op = operator.neg
    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')
        if insert_index <= 0:
            op = operator.pos
        if insert_index >= depth - 1:
            op = operator.neg
        insert_index += op(1)

    return result






# --------------------------------------------------------------
"""
1. Maximum subarray sum
Input [1, 3, -1, -2, 4, 5, 7, -10, -1, 2]
Output 16 (1 + 3 - 1 - 2 + 4 + 5 + 7)

2. Maximum circular subarray sum
Input [1, 3, -1, -2, 4, 5, 7, -10, -1, 2]
Output 19 (1 + 3 - 1 - 2 + 4 + 5 + 7 + 2)
"""
# --------------------------------------------------------------------
from typing import List


def get_max_sequence_sum(numbers: List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0
    # for文で和を足していって、その和が最大の瞬間を取っておけるようにif文で条件分岐する
    for num in numbers:
        temp_sum_sequence = sum_sequence + num
        if num < temp_sum_sequence:
            sum_sequence = temp_sum_sequence
        else:
            sum_sequence = num
        if result_sequence < sum_sequence:
            result_sequence = sum_sequence

    return result_sequence


def find_max_circular_sequence_sum(numbers: List[int]) -> int:
    # ①連続して最も小さくなる数字群を見つけ出して、全体の和から引く発想
    invert_numbers = []
    all_sum = 0
    for num in numbers:
        all_sum += num
        invert_numbers.append(-num)

    max_wrap_sequence = all_sum - (-get_max_sequence_sum(invert_numbers))

    # ②リストの端同士で最小の数字群の作る場合はそのままget_max_sequence_sumを使って最大が求まる
    max_sequence_sum = get_max_sequence_sum(numbers)

    # ①と②を比べて大きい方を戻り値とする
    return max(max_sequence_sum, max_wrap_sequence)





# ------------------------------------------------------------
# 重複を削除する
# ------------------------------------------------------------

# 重複は集合setを使えばすぐに消せる
l = [1,3,3,5,5,7,7,7,10,12,12,15]
print(list(set(l)))
# また辞書型に用意されているメソッドであるfromkeysを使ってもすぐできる
# fromkeysは引数に受けたリストをkeyにしてdict型を作ってくれる
print(list(dict.fromkeys(l)))

# リスト内包括でもできる
# if文でループの手前で重複がないことをnot in を用いて条件付けている
print([n for i in enumerate(l) if n not in l[:i]])


def delete_duplicate_v1(numbers: List[int]) -> None:
    temp = []
    for num in numbers:
        if num not in temp:
            temp.append(num)
    numbers[:] = temp


def delete_duplicate_v2(numbers : List[int]) -> None:
    temp = [numbers[0]]
    i , len_num = 0, len(numbers) - 1
    while i < len_num:
            if numbers[i] != numbers[i+1] 
            temp.append(numbers[i+1])
        i += 1
    numbers[:] = temp


def delete_duplicate_v3(numbers : List[int]) -> None:
    i = 0
    # removeを使うときはリストのインデックスがずれるのでその都度インデックス番号を調整する必要がある
    while i < len(numbers) -1:
        if numbers[i] == numbers[i+1]:
            numbers.remove(numbers[i])
            i -= 1
        i+=1

    # v3のコードはwhileの条件をループごとに計算し直す必要があるのであまり良いコードとは言えない
    








if __name__ == '__main__':
    print(list_to_int_plus_one([0, 0, 0, 9, 9, 9, 9, 9, 9]))

# joinメソッドでリストの中身をつなげる delimiter を最初に指定する
# list = ['A', 'B', 'C']
# print(''.join(list))
# # ABC
# s = ','.join(list)
# print(s)
# # A,B,C
# join関数はリストの要素がstr型でないと使えない。int型のときは
# list = ['A', 'B', 'C', 1, 2, 3]
# map = map(str, list)
# print(''.join(map))
# # ABC123
# とmap関数を用いて型変換する
    l = []
    for j in range(5):
        for i in range(10):
            l.append(i)
    numbers = [str(i) for j in range(5) for i in range(10)]
    for line in snake_stirng_v1(numbers):
        print(''.join(line))


    numbers = [str(i) for i in range(30)]
    for line in snake_string_v2(numbers, 5):
        print(''.join(line))

    print(find_max_circular_sequence_sum([1,-2,3,6,-1,2,4,-5,2]))
