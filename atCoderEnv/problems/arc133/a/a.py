#!/usr/bin python
N = input()
A = list(map(int, input().split()))
# A_set = set(A)

# result = "z"

# for x in A_set:
#     temp = " ".join([str(i) for i in A if i != x])
#     result = min(result, temp)

# print(result)





# 先頭の二つに注目する必要がある
no_overlapped_A = list(set(A))
if len(no_overlapped_A) >= 2:
    if str(no_overlapped_A[0]) < str(no_overlapped_A[1]):
        x = max(A)
        print(" ".join([str(i) for i in A if i != x]))    
    else:
        x = no_overlapped_A[0]
        print(" ".join([str(i) for i in A if i != x])) 
else:
    x = max(A)
    print(" ".join([str(i) for i in A if i != x]))

# 1番目に大きい数を抜いたものが最も良いのでは？？
# x = max(A)
# print(" ".join([str(i) for i in A if i != x]))