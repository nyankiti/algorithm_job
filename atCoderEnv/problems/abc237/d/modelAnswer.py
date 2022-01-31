L=[]
R=[]
N=int(input())
S=input()
for i,c in enumerate(S):
    print(i)
	# if c == 'L':
    #     R.append(i)
	# else:
    #     L.append(i)
    if c == "L":
        R.append(i)
    else:
        L.append(i)

print(*(L+[N]+R[::-1]))