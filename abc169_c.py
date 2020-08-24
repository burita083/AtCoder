import math
from decimal import Decimal

A, B = map(str, input().split())
A = Decimal(A)
B = Decimal(B)

print(math.trunc(A*B))