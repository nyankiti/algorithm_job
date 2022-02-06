S = input()
# stripは指定した文字を切り抜いた文字を返す
l = len(S) - len(S.lstrip('a'))  # 先頭の連続数
r = len(S) - len(S.rstrip('a'))  # 末尾の連続数
if l > r: 
    print("No")
else:
    T = "a" * (r - l) + S
    if T == T[::-1]:
        print("Yes")
    else:
        print("No")

