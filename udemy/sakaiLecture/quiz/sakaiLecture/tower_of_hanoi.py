# A B C
from typing import List, Tuple


def hanoi_myans(disk: int, src: str, dest, support: str):
    if disk == 1:
        return 1
    return hanoi(disk-1, src, support, dest) + hanoi(disk-1, support, dest, src) + 1


def hanoi(disk: int, src: str, dest: str, support: str):
    if disk < 1:
        return
    hanoi(disk-1, src, support, dest)
    print(f'move {disk} from {src} to {dest}')
    hanoi(disk-1, support, dest, src)


def get_hanoi_movement(disk: int, src: str, dest: str, support: str):
    result = []

    def _hanoi(disk: int, src: str, dest: str, support: str):
        if disk < 1:
            return
        _hanoi(disk-1, src, support, dest)
        result.append((disk, src, dest))
        _hanoi(disk-1, support, dest, src)

    _hanoi(disk, src, dest, support)
    print(len(result))
    return result


if __name__ == '__main__':
    print(get_hanoi_movement(6, "A", "B", "C"))
