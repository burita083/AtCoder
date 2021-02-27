a, b, c, d = map(int, input().split())

ans = 0


A = a*c
B = a*d
C = b*c
D = b*d 
ans = max(A,B)
ans = max(ans,C)
ans = max(ans,D)
print(ans)