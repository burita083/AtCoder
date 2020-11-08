def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)
N = int(input())
k = len(str(N))
l = list(str(N))
if N % 3 == 0:
  print(0)
  exit()

ans = digitSum(N)

import itertools
for i in range(1, k+1)[::-1]:
  for c in itertools.combinations(l, i):
    #now = ans-amari
    #while (now > 0):
    num_l = list(map(int, c))
    if sum(num_l) % 3 == 0:
      print(k-i)
      exit()
    #now -= 3

print(-1)