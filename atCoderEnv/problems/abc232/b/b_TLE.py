from sys import stdin
import string
from typing import Generator, Tuple

S = input()
T = input()


def caesar_cipher_hack(text: str) -> Generator[Tuple[int, str], None, None]:
    len_alphabet = ord("z") - ord("a") + 1
    # len_alphabet = ord(string.ascii_lowercase)

    for candidate_shift in range(1, len_alphabet + 1):
        reverted = ""
        for char in text:
            alphabet = string.ascii_lowercase

            # mod算術を用いることで、z以降のindexに対応する
            index = (alphabet.index(char) - candidate_shift) % len(alphabet)
            reverted += alphabet[index]
        yield candidate_shift, reverted


for candidate in caesar_cipher_hack(S):
    if candidate[1] == T:
        print("Yes")
        break
else:
    print("No")
