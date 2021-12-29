import string
import random

ALPHABET = string.ascii_uppercase


class PlugBoard(object):
    def __init__(self, map_alphabet):
        self.alphabet = ALPHABET
        self.forward_map = {}
        self.backward_map = {}
        self.mapping(map_alphabet)

    def mapping(self, map_alphabet):
        # "ABCD" => "BADC" と対応つける
        # {"A": "B", "B": "A", "C": "D", "D": "C"}
        self.forward_map = dict(zip(self.alphabet, map_alphabet))
        # forwardとkey valueが逆のdictを生成する
        self.backward_map = {v: k for k, v in self.forward_map.items()}

    def forward(self, index_num):
        char = self.alphabet[index_num]
        char = self.forward_map[char]
        # roterに対応するため、文字ではなくindex番号を返す
        return self.alphabet.index(char)

    def backward(self, index_num):
        char = self.alphabet[index_num]
        char = self.backward_map[char]
        # roterに対応するため、文字ではなくindex番号を返す
        return self.alphabet.index(char)


# PlugBoradを継承させるので、forward, backwordの動きは実装する必要がない
class Rotor(PlugBoard):
    def __init__(self, map_alphabet, offset=0):
        super().__init__(map_alphabet)
        self.offset = offset
        self.rotations = 0

    def rotate(self, offset=None):
        if offset is None:
            offset = self.offset
        # offset分 alphabetのずらす
        self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
        self.rotations += offset
        return self.rotations

    def reset(self):
        self.rotations = 0
        self.alphabet = ALPHABET


class Reflector(object):
    def __init__(self, map_alphabet):
        self.map = dict(zip(ALPHABET, map_alphabet))
        # 引数で受け取るmap_alphabetがreflectorに対応するようにkeyとvalueが一対一になっているかどうかをチェックする
        for x, y in self.map.items():
            if x != self.map[y]:
                raise ValueError(x, y)

    def reflect(self, index_num):
        reclected_char = self.map[ALPHABET[index_num]]
        return ALPHABET.index(reclected_char)


class EnigmaMachine(object):
    def __init__(self, plug_board, rotors, reflector):
        self.plug_board = plug_board
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, text):
        a = "".join([self.go_throufh(c) for c in list(text)])
        return a

    def decrypt(self, text):
        for rotor in self.rotors:
            rotor.reset()
        return "".join([self.go_throufh(c) for c in list(text)])

    def go_throufh(self, char):
        char = char.upper()
        if char not in ALPHABET:
            return char

        index_num = ALPHABET.index(char)

        index_num = self.plug_board.forward(index_num)
        # 行き道のrotor
        for rotor in self.rotors:
            index_num = rotor.forward(index_num)

        # 中間地点のreflector
        index_num = self.reflector.reflect(index_num)

        # 帰り道のrotor
        for rotor in reversed(self.rotors):
            index_num = rotor.backward(index_num)

        index_num = self.plug_board.backward(index_num)
        char = ALPHABET[index_num]

        # 次の暗号化のためのrotorの回転
        for rotor in reversed(self.rotors):
            if rotor.rotate() % len(ALPHABET) != 0:
                break

        return char


if __name__ == "__main__":
    # plug boardの動作確認---------------------------------------------
    plug_board = PlugBoard("BADC")
    encrypted_index = plug_board.forward(ALPHABET.index("A"))
    # Aを暗号化した際に文字
    print(ALPHABET[encrypted_index])

    decrypted_index = plug_board.backward(encrypted_index)
    print(ALPHABET[decrypted_index])

    # ----------------------------------------------------------------

    # rotorの動作確認---------------------------------------------
    rotor = Rotor("BADC", 3)
    encrypted_index = rotor.forward(ALPHABET.index("A"))
    # Aを暗号化した際に文字
    print(ALPHABET[encrypted_index])

    decrypted_index = rotor.backward(encrypted_index)
    print(ALPHABET[decrypted_index])

    rotor.rotate()

    encrypted_index = rotor.forward(ALPHABET.index("A"))
    # Aを暗号化した際に文字
    print(ALPHABET[encrypted_index])

    decrypted_index = rotor.backward(encrypted_index)
    print(ALPHABET[decrypted_index])
    # -----------------------------------------------------------------

    # reflectorの動作確認---------------------------------------------
    r = Reflector("BADC")
    i = r.reflect(ALPHABET.index("A"))
    print(ALPHABET[i])
    # ----------------------------------------------------------------

    # Enifma machineの動作確認---------------------------------------------
    print("Enigma Machine Test --------------------------")
    # random.sampleメソッドは指定したイテラブルなオブジェクトから指定した数だけ、重複なしでランダムに抽出し、listを返してくれる。
    # 以下の場合では、alphabetを並び替えただけとなる

    def get_random_alphabet(): return "".join(
        random.sample(ALPHABET, len(ALPHABET)))

    p = PlugBoard(get_random_alphabet())
    r1 = Rotor(get_random_alphabet(), 3)
    r2 = Rotor(get_random_alphabet(), 2)
    r3 = Rotor(get_random_alphabet(), 1)

    # reflectorで利用可能な一対一対応するalphabetの生成
    # 整列したalphabeの配列から、一対一対応で場所を入れ替えていくことで生成する
    r = list(ALPHABET)  # この時点ではaから順番に並んだalphbetが入る
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes)/2)):  # 一組ずつ入れ替えていく
        x = indexes.pop(random.randint(0, len(indexes)-1))
        y = indexes.pop(random.randint(0, len(indexes)-1))
        r[x], r[y] = r[y], r[x]

    reflector = Reflector("".join(r))

    machine = EnigmaMachine(p, [r1, r2, r3], reflector)
    plain_text = "ATTACK SILICON VALLEY"
    encrypted_text = machine.encrypt(plain_text)
    print(encrypted_text)
    decrypted_text = machine.decrypt(encrypted_text)
    print(decrypted_text)
    # ----------------------------------------------------------------
