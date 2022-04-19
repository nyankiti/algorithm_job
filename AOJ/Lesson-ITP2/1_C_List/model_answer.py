from sys import stdin

"""
一つの配列で管理すると、cursorを用いた配列へのアクセスが多すぎてLTEになる
=> cursorの前後で二つの配列を用意することで対応
"""

def main():
    N = int(stdin.readline())
    
    front = []
    back = []

    for _ in range(N):
        *query, = map(int, stdin.readline().split())
        if query[0] == 0:
            # insert
            back.append(query[1])
            pass
        elif query[0] == 1:
            # move
            d = query[1]
            if d > 0:
                for _ in range(d):
                    front.append(back[-1])
                    back.pop()
            else:
                for _ in range(-d):
                    back.append(front[-1])
                    front.pop()
        else:
            back.pop()

    for val in front:
        print(val)
    for val in reversed(back):
        print(val)



if __name__ == '__main__':
    main()
