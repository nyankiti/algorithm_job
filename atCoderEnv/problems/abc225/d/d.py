from sys import stdin
from collections import deque


class Train:
    def __init__(self) -> None:
        self.front = None
        self.back = None

    def front_connect(self, index):
        self.front = index

    def front_detach(self):
        self.front = None

    def back_connect(self, index):
        self.back = index

    def back_detach(self):
        self.back = None


def main():
    N, Q = map(int, stdin.readline().split())

    trains = [Train() for _ in range(N+1)]

    for _ in range(Q):
        q_type, *nums, = map(int, stdin.readline().split())

        if q_type == 1:
            x, y = nums
            trains[x].back_connect(y)
            trains[y].front_connect(x)

        elif q_type == 2:
            x, y = nums
            trains[x].back_detach()
            trains[y].front_detach()

        elif q_type == 3:
            x = nums[0]

            dq = deque()
            dq.append(x)
            target_tranin = trains[x]
            count = 1
            # backの取得

            next_index = target_tranin.back
            while next_index:
                count += 1
                dq.append(next_index)
                next_index = trains[next_index].back

            # frontの取得
            next_index = target_tranin.front
            while next_index:
                count += 1
                dq.appendleft(next_index)
                next_index = trains[next_index].front

            print(count, *dq)


if __name__ == '__main__':
    main()
