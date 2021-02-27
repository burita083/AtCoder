import itertools
N = int(input())
ans = 0
for i in range(1, 10):
  for x in itertools.product("753", repeat=i):
    s= ''.join(x)
    if int(s) > N: continue
    if '3' not in s: continue
    if '5' not in s: continue
    if '7' not in s: continue
    ans += 1
print(ans)