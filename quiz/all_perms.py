from typing import List, Iterator


# 順列を全て表示するプログラム
def all_perms(elements: List[int]) -> Iterator[List[int]]:
    if len(elements) <= 1:
        yield elements
    else:
        rest = elements[1:]
        first = elements[0:1]

        for perm in all_perms(rest):
            for i in range(len(elements)):
                yield perm[:i] + first + perm[i:]


if __name__ == "__main__":
    for p in all_perms([2, 3, 4]):
        print(p)
