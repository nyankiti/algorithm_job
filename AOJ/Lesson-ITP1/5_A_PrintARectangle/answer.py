# while True:
#     H, W = map(int, input().split())
#     if H == 0 and W == 0:
#         break
#     for _ in range(H):
#         print("#"*W)
#     print()


# while True:
#     H, W = map(int, input().split())
#     if H == 0 and W == 0:
#         break

#     print("#"*W)
#     for _ in range(H-2):
#         print("#", end="")
#         print("."*(W-2), end="")
#         print("#")
#     print("#"*W)
#     print()

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    result = []
    for i in range(H):
        temp = []
        if i % 2 == 1:
            for j in range(W):
                if j % 2 == 0:
                    temp.append(".")
                else:
                    temp.append("#")
        else:
            for j in range(W):
                if j % 2 == 0:
                    temp.append("#")
                else:
                    temp.append(".")
        result.append(temp)
    for row in result:
        print("".join(row))
    print()
