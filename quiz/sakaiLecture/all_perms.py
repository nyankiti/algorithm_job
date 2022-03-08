from typing import List, Iterator
from unittest import result


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

# yieldを用いないversion
def all_perms_v2(elements: List[int]) -> List[List[int]]:
    result = []
    if len(elements) <= 1:
        return [elements]

    first = elements[0:1]    
    rest = elements[1:]

    for perm in all_perms_v2(rest):
        for i in range(len(elements)):
            result.append((perm[:i] + first + perm[i:]))

    return result

if __name__ == "__main__":
    # for p in all_perms([2, 3, 4]):
    #     print(p)

    for p in all_perms_v2([1,2,3,4]):
        print(p)
