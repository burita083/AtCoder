N, X, M = map(int, input().split())
A = [X]
seen = [0] * (M + 1)
seen[X] = 1
N -= 1
while N:
    a = (A[-1] ** 2) % M
    if seen[a]:
        i = A.index(a)
        break
    else:
        A.append(a)
        seen[a] = 1
        N -= 1
if N:
    loop = len(A) - i
    q, r = divmod(N, loop)
    print(sum(A) + sum(A[i:]) * q + sum(A[i:i+r]))
else:
    print(sum(A))
