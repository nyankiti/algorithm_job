from typing import List

def generate_pascal_triangle_by(depth: int) -> List[List[int]]:
  data = [[1] * (i + 1) for i in range(depth)]

  for i in range(depth):
    inner_len = len(data[i])
    for j in range(inner_len):
      if j == 0 or j == inner_len:
        continue
      data[i][j] = data[i-1][j-1] + data[i-1][j]

  print(data)


def generate_pascal_triangle(depth: int) -> List[List[int]]:
  data = [[1] * (i + 1) for i in range(depth)]

  for line in range(2,depth):
    for i in range(1,line):
      data[line][i] = data[line-1][i-1] + data[line-1][i]

  return data

def print_pascal(data: List[int]) -> None:
  for index, line in enumerate(data):
    numbers = ''.join([str(i).center(6, ' ') for i in line])
    print((' '*int(3))*(len(data) - index), numbers)

if __name__ == '__main__':

  print_pascal(generate_pascal_triangle(5))