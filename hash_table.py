import hashlib
from typing import Any

# dict型のインデックス番号割り振りのときにハッシュ関数が使われるのでハッシュテーブルと呼ばれる
class HashTable(object):

    def __init__(self, size=10) -> None:
        self.size = size
        # sizeに合わせた数の配列として管理される
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        hash_str = hashlib.md5(key.encode()).hexdigest()
        # 16進数文字列であるhash_strをintに変換するために、第二引数にbase=16を指定する(defaultはbase=10)
        hash_int = int(hash_str, base=16)
        return hash_int % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        # hash table値も二つの要素を持つ配列として管理する
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            # printメソッドのendを指定することで、defaultの改行コードから上書きされるので、改行されなくなる
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')

            # 改行するための空printを実行
            print()

    def get(self, key) -> Any:
        index = self.hash(key)
        # 以下のように値を探す際に、hashを用いてtableを管理しているので、そのtableの中から効率的に値を探すことができる。 
        # => 値を参照する際の計算効率がとてもよくなる
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    # 特殊なattributeを用いて hash_table['car'] = 'Telsa' のような値の追加方法を実装する
    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, key) -> Any:
        return self.get(key)


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table['car'] = 'Telsa'
    hash_table['car'] = 'Toyota'
    hash_table['pc'] = 'Mac'
    hash_table['sns'] = 'YouTube'
    hash_table.print()
    print(hash_table['sns'])
