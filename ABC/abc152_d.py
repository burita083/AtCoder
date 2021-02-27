N = int(input())
count = [[0]*10 for i in range(10)]
for n in range(1, N+1):
    count[int(str(n)[0])][int(str(n)[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += count[i][j] * count[j][i]
print(ans)