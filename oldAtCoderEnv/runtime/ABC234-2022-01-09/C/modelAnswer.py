# 条件を満たす整数の中でK番目に小さいものは、Kを2進数表現にした後に、そこに現れる1を2に置き換えたもの！！

K = int(input())

# Kを二進数に変換し、その後1と2を入れ替える 1行で解説完了
print(format(K, "b").replace("1", "2"))

# 二進数への変換を自分で実装


def convertbinaryDigits(num):
    result = []
    while num > 0:
        result.append(num % 2)
        num = num // 2
    result.reverse()
    return "".join(list(map(str, result)))


bin_K = convertbinaryDigits(K)
print(bin_K.replace("1", "2"))
