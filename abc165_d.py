A, B, N = map(int, input().split())

mn = min(N, B-1)
print(A*mn//B-A*(mn//B))