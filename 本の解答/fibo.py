def tribo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  cache = {}
  if cache.get(n) is None:
    cache[n] = tribo(n-1)+tribo(n-2)+tribo(n-3)
  return cache[n]
  


if __name__ == "__main__":
  print(tribo(10))