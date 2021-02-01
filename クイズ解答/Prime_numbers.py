from typing import List

def generate_primes_v1(numbers: List[int]) -> List[int]:
  primes = []
  for x in range(2, numbers + 1):
    # 調べている数の手前までの数でひたすら割ることで素数かどうかを調べる
    for y in range(2,x):
      if x % y == 0:
        break
    else:
        primes.append(x)

  return primes



def generate_primes_v2(numbers: List[int]) -> List[int]:
  primes = []
  # ある素数を見つけたときにその倍数をcacheに入れることでループの数を減らす
  cache = {}
  for x in range(2, numbers + 1):
    is_prime = cache.get(x)
    if is_prime is False:
      # for分を一度とばすcontinue
      continue
    primes.append(x)
    cache[x] = True
    # 倍数をキャッシュに記録
    for y in range(x*2, numbers+1, x):
      cache[y] = False
  return primes




if __name__ == "__main__":
  # time モジュールを用いて各メソッドの計算効率を可視化する
  import time
  # start = time.time()
  # print(generate_primes_v1(50))
  # print(time.time() - start)

  start = time.time()
  print(generate_primes_v2(10000))
  print(time.time() - start)
