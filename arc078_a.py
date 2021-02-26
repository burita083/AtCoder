N = int(input())

A = list(map(int, input().split()))

sm = 0
cums = [0]
for a in A:
  sm += a
  cums.append(sm)

mn = float('inf')
if len(cums) == 2:
  print(abs(A[0]-A[1]))
  exit()
for i in range(1, N):
  snuke = cums[i]-cums[0]
  araiguma = sm-snuke
  mn = min(mn, abs(snuke-araiguma))
print(mn)

