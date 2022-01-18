from typing import List, Iterator


def bitFullSearch(item) -> Iterator[List[str]]:
    len_item = len(item)
    for i in range(2 ** len_item):
        bag = []
        # print("pattern {}: ".format(i), end="")
        for j in range(len_item):
            if ((i >> j) & 1):
                bag.append(item[j][0])
        yield bag


if __name__ == '__main__':

    money = 300
    item = [("みかん", 100), ("りんご", 200), ("ぶどう", 300),
            ("さくらんぼ", 150), ("バナナ", 170), ("りんご", 120)]

    for pattern in bitFullSearch(item):
        print(pattern)
