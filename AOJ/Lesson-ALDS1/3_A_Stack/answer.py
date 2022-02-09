# 逆ポーランド記法(RPN: Reverse Polish Notation)の計算をstackを用いて計算する
RPN = input().split()
operators = ["+", "-", "*"]


def operate(int1, int2, op):
    if op == "+":
        return int2 + int1
    elif op == "-":
        return int2 - int1
    else:
        return int2 * int1


stack = []
for elem in RPN:
    if elem in operators:
        result = operate(int(stack.pop()), int(stack.pop()), elem)
        stack.append(result)
    else:
        stack.append(elem)

print(stack.pop())


# コードを簡潔にしたバージョン---------------------------------------------------
# in の使い方や、evalの使い方がとても勉強になる、、、、
st = []
for elem in input().split():
    if elem in "+-*":
        v2 = st.pop()
        v1 = st.pop()
        st.append(str(eval(v1 + elem + v2)))
    else:
        st.append(elem)
print(st[0])
