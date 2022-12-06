from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    T = input()

    li = []
    li_rev = []
    step = 0
    step_rev = 0
    for i in range(len(S)):
        if i+step < len(T) and S[i] != T[i+step]:
            li.append(i+1)
            step += 1
        if S[-i-1] != T[-i-1-step_rev]:
            li_rev.append(len(S)-i+1)
            step_rev += 1
    # print(len(S))
    # print(li)
    # print(li_rev)
    if len(li+li_rev) > 0:
        for ans_candi in li+li_rev:
            if S[:ans_candi-1]+T[ans_candi-1]+S[ans_candi-1:] == T:
                print(ans_candi)
                return
    else:
        # 最後の一つの可能性
        if S+T[-1] == T:
            print(len(T))


if __name__ == '__main__':
    main()
