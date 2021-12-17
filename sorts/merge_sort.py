from typing import List


# def merge_sort(numbers: List[int]) -> List[int]:
#     if len(numbers) <= 1:
#         return numbers

#     center = len(numbers) // 2
#     left = numbers[:center]
#     right = numbers[center:]

#     merge_sort(left)
#     merge_sort(right)

#     i = j = k = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             numbers[k] = left[i]
#             i += 1
#         else:
#             numbers[k] = right[j]
#             j += 1
#         k += 1

#     while i < len(left):
#         numbers[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         numbers[k] = right[j]
#         j += 1
#         k += 1

#     return numbers

# 2021 12 14
def merge_sort(numbers : List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    left_index = right_index = result_index = 0

    while left_index < len(left) and right_index < len(right) :
        if (left[left_index] <= right[right_index]):
            numbers[result_index] = left[left_index]
            left_index += 1
        else:
            numbers[result_index] = right[right_index]
            right_index += 1
        result_index += 1
    
    while left_index < len(left):
        numbers[result_index] = left[left_index]
        left_index += 1
        result_index += 1
    
    while right_index < len(right):
        numbers[result_index] = right[right_index]
        right_index += 1
        result_index += 1
    
    return numbers



if __name__ == '__main__':
    import random
    # nums = [random.randint(0, 1000) for _ in range(10)]
    nums = [9, 8,7,6,5,4,3]
    print(merge_sort(nums))