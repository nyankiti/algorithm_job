from sys import stdin

n = int(stdin.readline())
*A, = map(int, stdin.readline().split())

comp_count = 0


def merge(numbers, left, right):
    global comp_count

    left_index = right_index = result_index = 0
    len_left, len_right = len(left), len(right)

    while left_index < len_left and right_index < len_right:
        if (left[left_index] <= right[right_index]):
            numbers[result_index] = left[left_index]
            left_index += 1
        else:
            numbers[result_index] = right[right_index]
            right_index += 1
        result_index += 1

    while left_index < len_left:
        numbers[result_index] = left[left_index]
        left_index += 1
        result_index += 1

    while right_index < len_right:
        numbers[result_index] = right[right_index]
        right_index += 1
        result_index += 1

    comp_count += (len_right + len_left)


def merge_sort(numbers):
    global comp_count
    if len(numbers) <= 1:
        return numbers
    if len(numbers) == 2:
        comp_count += 2
        if numbers[0] < numbers[1]:
            return numbers
        else:
            numbers[0], numbers[1] = numbers[1], numbers[0]
            return numbers

    center = len(numbers) // 2
    left_numbers = numbers[:center]
    right_numbers = numbers[center:]

    merge_sort(left_numbers)
    merge_sort(right_numbers)

    merge(numbers, left_numbers, right_numbers)

    return numbers


merge_sort(A)
print(*A)
print(comp_count)
