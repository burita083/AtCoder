A = int(input())
from collections import Counter
C = Counter([])
for i in range(1, int(A+1)):
  sm = i*(i+1)//2
  if C[sm-A] == 1:
    print("YES")
    exit()
  C[sm] = 1

print("No")