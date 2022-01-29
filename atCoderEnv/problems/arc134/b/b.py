#!/usr/bin python
N = int(input())
string_arr = list(input())
sub_arr = []
 
# selection sortの応用で解ける
for i in range(N//2 + 1):
    min_index = i
    for j in range(i+1, N):
        if string_arr[min_index] >= string_arr[j]:
            min_index = j
    
    if i == 0:
        string_arr[min_index], string_arr[i] = string_arr[i], string_arr[min_index]
        sub_arr.insert(len(sub_arr)-i, min_index)
        sub_arr.insert(i, i)
    else:
        if sub_arr[len(sub_arr)-i] >= min_index: 
            string_arr[min_index], string_arr[i] = string_arr[i], string_arr[min_index]
            sub_arr.insert(len(sub_arr)-i, min_index)
            sub_arr.insert(i, i)
 
print("".join(string_arr))