# O(log(n))
def func2(n):
  if n <= 1:
    return
  else:
    print(n)
    # 関数の中でもう一度その関数を呼ぶ再帰的なプログラムはO(log(n))となる事が多い
    func2(n/2)
  
# n = 10で試すと、この関数は4回再帰される
func2(10)
# n = 100で試すと、この関数は7回再帰される
func2(100)
# n = 100で試すと、この関数は10回再帰される
func2(1000)
# このような増え方がO(log(n))

# ----------------------------------------------------------
# O(n)
def func3(numbers):
  for num in numbers:
    print(num)


# ------------------------------------------------------------
# O(n * log(n))
def func4(n):
  # int(n)で再帰した時のnの小数点を切り捨てている
  for i in range(int(n)):
    # print関数の第二引数で改行を制限できる
    print(i, end=' ')
# 空白をprintすることで改行になる
  print()

  if n <= 1:
    return 
  func4(n/2)

func4(10)

# ---------------------------------------------------
# O(n**2)
def func5(numbers):
  for i in range(len(numbers)):
    for j in range(len(numbers)):
      print(numbers[i], numbers[j])
    print()

func5([1, 2, 3, 4, 5])