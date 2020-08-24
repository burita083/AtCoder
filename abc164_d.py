S = input()
r = 1
arr = [0]

for c in S[::-1]:
  arr.append((arr[-1] + int(c) * r) % 2019)
  r *= 10
  r %= 2019
print(arr)
from collections import Counter
ctr = Counter(arr)
ans = 0
print(ctr)
for v in ctr.values():
  ans += v*(v-1)//2
print(ans)