K = int(input())

ans = 0
for a in range(1, 10**6+1):
    if a > K: break
    BC = K//a
    for b in range(1, 10**6+1):
        if a * b > K:break
        C = BC//b
        ans += C
print(ans)