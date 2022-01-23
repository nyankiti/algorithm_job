# 参考
# https://atcoder.jp/contests/arc133/editorial/3284
n=int(input())
a=list(map(int,input().split()))
 
x=a[-1]
for i in range(n-1):
	if a[i]>a[i+1]:
		x=a[i]
        # 最も先頭に近いものを取るので、一つ見つかった時点でbreakする
		break
 
a=[v for v in a if v!=x]
print(*a)