N = int(input())
import math
A = []
for _ in range(N):
  x, y = map(int, input().split())
  A.append((x, y))
 

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

for i in range(len(A)-2):
  for j in range(i+1, len(A)-1):
    for k in range(j+1, len(A)):
      AB = get_distance(A[i][0], A[i][1], A[j][0], A[j][1])
      AC = get_distance(A[i][0], A[i][1], A[k][0], A[k][1])
      BC = get_distance(A[j][0], A[j][1], A[k][0], A[k][1])
      
      if (abs(AB) + abs(AC) == abs(BC)) or (abs(AB) + abs(BC) ==  abs(AC)) or (abs(AC) + abs(BC) == abs(AB)):
        if AB**2 + AC**2 == BC**2:
          continue

        if AB**2 + BC**2 == AC**2:
          continue

        if AC**2 + BC**2 == AB**2:
          continue

        print("Yes")
        exit()

print("No")