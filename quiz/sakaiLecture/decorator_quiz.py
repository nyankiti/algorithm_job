# そもそもデコレーターとは
# 主に、既存の関数の実装自体は 変更せずに 、その関数に追加の処理を加える目的で作られる関数。処理追加対象の関数を引数として受け取り、追加処理を実装した新たな関数を返す
# ある処理の前後に処理を入れられる関数のようなもの

def memoize(f):
  def _wrapper(n):
    print('before')
    r = f(n)
    print('after')
    return r
  return _wrapper

@memoize
def test(n):
  print('test')

print(test(10))

