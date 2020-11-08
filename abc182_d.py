N = int(input())

A = list(map(int, input().split()))

ans = 0
from itertools import accumulate
S = [0]+list(accumulate(A))
m = max(S)
index = S.index(max(S))

for i in range(N-1):
  ans += S[i+1]-S[0]

for i in range(index):
  ans += S[i]

if ans >= 0:
  print(ans)
else:
  print(0)
#print(S)

#for i in range(len(A)):
  #for j in range(i+1):
    #ans += A[j]
    #mx = max(mx, ans)
    #print(ans, i, "aaaa")

#print(mx)
