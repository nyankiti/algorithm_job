from sys import stdin, exit

# "#" => 黒, "." => 白
n = int(stdin.readline())

grid = []

for i in range(n):
    grid.append(input())

def horizontal_traversal(grid):
    if n == 6:
        for row in grid:
            if row.count("#") >= 4:
                return True
        return False
    else:
        for row in grid:
            for index in range(n-6):
                if row[index: index+6].count("#") >= 4:
                    return True
        return False


def diagonal_traversal(grid):
    for i in range(n):
        diagonal_arr = []
        tmp_i = i
        height = 0
        while height < n - i:
            diagonal_arr.append(grid[height][tmp_i])
            height += 1
            tmp_i += 1

        len_diagonal_arr = len(diagonal_arr)
        if len_diagonal_arr == 6:
            if diagonal_arr.count("#") >= 4:
                return True
        elif len_diagonal_arr > 6:
            # 探索
            for index in range(len_diagonal_arr-6):
                if diagonal_arr[index: index+6].count("#") >= 4:
                    return True
        else:
            # 長さが6より小さくなれば、探しても意味がない
            return False


def diagonal_traversal_down(grid):
    for i in range(n):
        diagonal_arr = []
        tmp_i = i
        height = 0
        while height < n - i:
            diagonal_arr.append(grid[tmp_i][height])
            height += 1
            tmp_i += 1
        
        len_diagonal_arr = len(diagonal_arr)
        if len_diagonal_arr == 6:
            if diagonal_arr.count("#") >= 4:
                return True
        elif len_diagonal_arr > 6:
            # 探索
            for index in range(len_diagonal_arr-6):
                if diagonal_arr[index: index+6].count("#") >= 4:
                    return True
        else:
            # 長さが6より小さくなれば、探しても意味がない
            return False

# 横の探索
if horizontal_traversal(grid):
    print("Yes")
    exit()

# 斜めの探索
if diagonal_traversal(grid):
    print("Yes")
    exit()

if diagonal_traversal_down(grid):
    print("Yes")
    exit()

# 縦の探索
grid_t = list(map(list, zip(*grid)))
if horizontal_traversal(grid_t):
    print("Yes")
    exit()

# 斜めの探索
if diagonal_traversal(grid_t):
    print("Yes")
    exit()

if diagonal_traversal_down(grid_t):
    print("Yes")
    exit()


print("No")