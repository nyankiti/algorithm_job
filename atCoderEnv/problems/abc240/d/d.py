from itertools import count
from sys import stdin
from collections import deque


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    dq = deque()

    prev_val = -1
    prev_prev_val = -1
    count = 1
    for a in A:
        if a == prev_val:
            count += 1
            if count == a:
                for _ in range(count-1):
                    dq.pop()
                prev_val = prev_prev_val

                # print("HUHUHU", dq)
                # 球が消えた際に、下で連続しているcountを数える
                count = 0
                if len(dq) > 1:
                    for i in range(1, len(dq)+1):
                        if dq[-i] == prev_val:
                            count += 1
                        else:
                            prev_prev_val = dq[-i]
                            break
                else:
                    count = 1
                # print("next_count", count)

            else:
                dq.append(a)
        else:
            dq.append(a)
            count = 1
            prev_prev_val = prev_val
            prev_val = a

        # print(dq)
        print(len(dq))


if __name__ == '__main__':
    main()
