N = int(input())

A = list(map(int, input().split()))
from collections import Counter
C = Counter(A)

s = "aiueo"
if len(C) > 4: 
    print("No")
    exit()

if len(C) == 3:
    s1, s2, s3 = set(C.keys())
    if s1 ^ s2 ^ s3 == 0 and C[s1] * 3 == N and C[s2] * 3 == N and C[s3] * 3 == N:
        print("Yes")
    else:
        print("No")
elif len(C) == 2:
    if C[0] > 0:
        if C[0] * 3 == N:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    if C[0] > 1:
        print("Yes")
    else:
        print("No")