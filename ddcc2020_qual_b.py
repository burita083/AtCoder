N = int(input())

A = list(map(int, input().split()))
sm = sum(A)
s = 0
smm = 0
l = [0]
for a in A:
  smm += a
  l.append(smm)

mn = float('inf')
for i in range(1,N):
  left = l[i] - l[0]
  right = smm - left
  mn = min(mn, abs(left-right))
print(mn)