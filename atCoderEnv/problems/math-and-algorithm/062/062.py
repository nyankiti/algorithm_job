from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    A = [0] + list(map(int, stdin.readline().split()))

    next = A[1]
    teleport_history = [1, next]

    visited = {
        1: True,
        next: True
    }

    loop_start = -1

    for _ in range(N):
        next = A[next]
        if visited.get(next):
            loop_start = next
            break

        visited[next] = True
        teleport_history.append(next)

    loop_start_index = teleport_history.index(loop_start)
    # print(teleport_history)
    # print(loop_start)
    # print(loop_start_index)

    if K <= loop_start_index:
        print(teleport_history[K])
    else:
        loop_list = teleport_history[loop_start_index:]
        loop_len = len(loop_list)
        print(loop_list[(K - loop_start_index) % loop_len])


if __name__ == '__main__':
    main()
