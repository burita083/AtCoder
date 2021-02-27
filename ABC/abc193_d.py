from collections import Counter
K = int(input())
S = input()
T = input()

Takahashi = list(S)
AOKI = list(T)

TC = Counter(Takahashi)
AC = Counter(AOKI)

d = {}
for i in range(1, 10):
  d[i] = K

card = 9*K
TakahashiSum = 0
for i in range(1, 10):
  if str(i) in TC.keys():
    TakahashiSum += i*(10**TC[str(i)])
    d[i] -= TC[str(i)]
  else:
    TakahashiSum += i

AokiSum = 0
for i in range(1, 10):
  if str(i) in AC.keys():
    AokiSum += i*(10**AC[str(i)])
    d[i] -= AC[str(i)]
  else:
    AokiSum += i

l = []

for i in range(1, 10):
  tempTakahashi = TakahashiSum
  tempAoki = AokiSum
  temp = d.copy()
  if temp[i] <= 0:continue
  temp[i] -= 1
  for j in range(1, 10):
    tempTakahashi = TakahashiSum
    tempAoki = AokiSum

    if temp[j] <= 0:continue
    if str(i) in TC.keys():
      tempTakahashi -= i*(10**TC[str(i)])
      tempTakahashi += i*(10**(TC[str(i)]+1))
    else:
      tempTakahashi +=  10*i 

    if str(j) in AC.keys():
      tempAoki -= j*(10**AC[str(j)])
      tempAoki += j*(10**(AC[str(j)]+1))
    else:
      tempAoki += 10*j
    
    if tempTakahashi > tempAoki:
      l.append((i, j))


ans = 0
remain = card - 8
print(l)
for ll in l:
  t = ll[0]
  a = ll[1]
  print(d[t], d[a])
  ans += (d[t]/remain)*(d[a]/(remain-1))
print(ans)



