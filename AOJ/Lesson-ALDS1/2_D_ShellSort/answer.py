n = int(input())
A = [int(input()) for _ in range(n)]

count = 0

def gap_insertion_sort(A, n, gap):
    global count

    for i in range(gap, n):
        temp = A[i]
        j = i - gap
        while j >= 0 and A[j] > temp:
            A[j+gap] = A[j]
            j -= gap
            count += 1
        A[j+gap] = temp


def shell_sort(A, n):
    global count
    count = 0
    g = 1
    G = [g]
    while 3 * g + 1 < n:
        g = 3 * g + 1
        G.append(g)
    m = len(G)
    G = G[::-1]

    print(m)
    print(*G)

    for j in G:
        gap_insertion_sort(A,n,j)


shell_sort(A, n)

print(count)
print(*A, sep="\n")