import bisect
t = int(input())
l = []
n = 2
l.append(2)
for x in range(2, 25822):
  n += 3*x-1
  l.append(n)

for n in range(t):
  a = int(input())
  ans = 0
  while True:
    tallest = bisect.bisect(l, a)
    a =  a - l[tallest-1]
    if a > 0: 
      ans += 1
    elif a < 0:
      print(ans)
      break
    else:
      ans += 1
