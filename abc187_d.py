N = int(input())

AOKI = []
T = []
a = 0
R = []
for x in range(N):
  A, B = map(int, input().split())
  AOKI.append((A+A+B, A))
  a += A
  T.append(A)
  R.append(a)
AOKI = sorted(AOKI)
T = sorted(T)

total = R.pop()
count = 0
AMax = 0
while True:
  tempA = AOKI.pop()
  AMax += tempA[0] - tempA[1]
  total -= tempA[1]
  if AMax > total:
    count += 1
    print(count)
    exit()
  count += 1


