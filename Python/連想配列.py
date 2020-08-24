a = int(input())
A = list(map(int, input().split()))  

"dictonary初期化"
d = {}
for k in A:
  "ある数値がどれだけあるかをカウントする。1が3個、2が2個等"
  if k in d:
    d[k] += 1
  else:
    d[k] = 1
 
res = 0

"valueを列挙する"
for k in d.values():
    if k >= 2:
      res += ncr(k, 2)

for k in A:
  temp = res
  m = d[k]
  if m >= 2:
    temp -= ncr(m, 2)

  d[k] -= 1
  if d[k] >= 2:
    temp += ncr(d[k], 2)
  print(temp)
  d[k] += 1

S = input()
T = input()
d = {}

for s, t in zip(S, T):
  if s in d:
    #含まれている場合で、tと異なるならば、変換ができないということ
    if d[s] != t:
      print("No")
      exit()
  else:
    d[s] = t

#keyの数に対し、valuesが重複していて、数が合わなければ、変換ができない
if len(d) != len(set(d.values())):
  print("No")
else:
  print("Yes")

