from typing import Generator, Tuple
import string


# カエサル式暗号　単純にアルファベットをシフトするだけの暗号
# stringライブラリを用いた方法
def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase  # abcdefghijklmnopqrstuvwxyz
        elif char.islower():
            alphabet = string.ascii_lowercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
        else:
            result += char
            continue

        # mod算術を用いることで、z以降のindexに対応する
        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]
    return result


# stringライブラリを使わずに組み込みのord, chrメソッドを用いる方法
def caesar_cipher_v2(text: str, shift: int) -> str:
    result = ""
    len_alphabet = ord("Z") - ord("A") + 1
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - ord("A")) %
                          len_alphabet + ord("A"))
        elif char.islower():
            result += chr((ord(char) + shift - ord("a")) %
                          len_alphabet + ord("a"))
        else:
            result += char
            continue

    return result


# ある暗号がある時、以下のメソッドによって複合候補を羅列し、その中から意味が通るものを目視で確認し、正解とする
def caesar_cipher_hack(text: str) -> Generator[Tuple[int, str], None, None]:
    len_alphabet = ord("z") - ord("a") + 1
    # len_alphabet = ord(string.ascii_lowercase)

    for candidate_shift in range(1, len_alphabet + 1):
        reverted = ""
        for char in text:
            if char.isupper():
                alphabet = string.ascii_uppercase
            elif char.islower():
                alphabet = string.ascii_lowercase
            else:
                reverted += char
                continue

                # mod算術を用いることで、z以降のindexに対応する
            index = (alphabet.index(char) - candidate_shift) % len(alphabet)
            reverted += alphabet[index]
        yield candidate_shift, reverted


def caesar_cipher_hack_v2(text: str) -> Generator[Tuple[int, str], None, None]:
    len_alphabet = ord("z") - ord("a") + 1

    for candidate_shift in range(1, len_alphabet + 1):
        reverted = ""
        for char in text:
            if char.isupper():
                reverted += chr((ord(char) - candidate_shift -
                                ord("A")) % len_alphabet + ord("A"))
            elif char.islower():
                reverted += chr((ord(char) + candidate_shift -
                                ord("a")) % len_alphabet + ord("a"))
            else:
                reverted += char
                continue

        yield candidate_shift, reverted


if __name__ == '__main__':
    e = caesar_cipher("ATTACK SILICON VALLY by engineer", 3)
    print(e)

    for candidate in caesar_cipher_hack_v2(e):
        print(candidate)
