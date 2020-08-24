def toggleKthBit(n, k): 
  return (n ^ (1 << (k-1))) 
def popcount(x):
    x -= (x >> 1) & 0x5555555555555555
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    return ((x * 0x0101010101010101) & 0xffffffffffffffff ) >> 56
N = int(input())
X = int(input())

ans = -1
dp = [-1] * 100000000
for i in range(N, 0, -1):
  count = 0
  ans = toggleKthBit((int(str(X), 2)), i)
  while ans != 0:
    if dp[ans] != -1:
      ans = ans % dp[ans]
    else:
      dp[ans] = popcount(ans)
      ans = ans % dp[ans]
    count += 1
  print(count)
