import string


# ヴィジョネル暗号は、plain textとkeyを用いて暗号化する暗号。

# keyとplain textは同じ長さが必要(リピートすることでkeyを引き伸ばす)
def generate_key_myans(message: str, keyword: str) -> str:
    key = ""

    while len(message) >= len(key):
        key += keyword

    if len(message) == len(key):
        return key
    else:
        diff = len(key) - len(message)
        return key[:len(key) - diff]


def generate_key(message: str, keyword: str) -> str:
    key = keyword
    remain_length = len(message) - len(keyword)
    for i in range(remain_length):
        # 以下のよにすると、繰り返しの度にkeyが長くなるので、out of index エラーにならない
        key += key[i]
    return key


def vigenere_chipher(message: str, keyword: str) -> str:
    result = ""
    key = generate_key(message, keyword)
    ALPHABET = string.ascii_uppercase

    for i, char in enumerate(message):
        if char not in ALPHABET:
            result += char
            continue

        index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
        result += ALPHABET[index]
        # ord, chrを用いた場合
        # result += chr((ord(message[i]) + ord(key[i])) %
        #               len(ALPHABET) + ord("A"))
    return result


def vigenere_chipher_hack(chipher_text: str, keyword: str) -> str:
    result = ""
    key = generate_key(chipher_text, keyword)
    ALPHABET = string.ascii_uppercase

    for i, char in enumerate(chipher_text):
        if char not in ALPHABET:
            result += char
            continue

        index = (ALPHABET.index(char) -
                 ALPHABET.index(key[i]) + len(ALPHABET)) % len(ALPHABET)
        result += ALPHABET[index]
        # ord, chrを用いた場合
        # result += chr((ord(chipher_text[i]) - ord(key[i]) +
        #               len(ALPHABET)) % len(ALPHABET) + ord("A"))
    return result


if __name__ == "__main__":
    plain_text = "ATTACK SILICON VALLY"

    e = vigenere_chipher(plain_text, "HELLO")
    print(e)

    d = vigenere_chipher_hack(e, "HELLO")
    print(d)
