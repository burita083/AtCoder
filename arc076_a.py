import math
def kaijou(n):
    if n==0:
        return 1
    else:
        return (n*kaijou(n-1))%MOD
N, M = map(int, input().split())

MOD = 10**9+7
if N == M:
  print((math.factorial(N)%MOD * math.factorial(M)%MOD * 2)%MOD)
elif N > M:
  if M >= N-1:
    print(math.factorial(N)%MOD * math.factorial(M)%MOD)
  else:
    print("0")
else:
  if N >= M-1:
    print(math.factorial(N)%MOD * math.factorial(M)%MOD)
  else:
    print("0")


