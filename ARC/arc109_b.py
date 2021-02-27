n = int(input())

ans = 0
for i in range(n+1):
    if i*(i+1)//2 <= n+1:
        ans = i
print(n-ans+1)