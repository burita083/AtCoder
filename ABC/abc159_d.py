def choose2(n):
    return n * (n - 1) // 2

a = int(input())
A = list(map(int, input().split()))  
d = {}
for k in A:
  if k in d:
    d[k] += 1
  else:
    d[k] = 1
 
res = 0
for k in d.values():
  res += choose2(k)

for k in A:
  temp = res
  m = d[k]
  temp -= choose2(m)

  d[k] -= 1
  temp += choose2(d[k])
  print(temp)
  d[k] += 1
