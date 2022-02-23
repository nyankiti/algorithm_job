
while True:
    a, op, b = list(input().split())
    if op == "?":
        break
    print(int(eval(a+op+b)))
