from sys import stdin, exit

N = int(stdin.readline())
used_numbers = [False]*(2*N+1)


while True:
    index = used_numbers.index(False)
    used_numbers[index] = True

    print(index+1, flush=True)
    # 入力の受け取り
    ans = int(stdin.readline())

    if ans == 0:
        exit()

    used_numbers[ans-1] = True
