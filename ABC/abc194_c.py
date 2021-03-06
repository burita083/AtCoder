N = int(input())

A = list(map(int, input().split()))

ans = 0
counter = [0 for _ in range(410)]
for a in A:
	counter[a+200] += 1
for i in range(409)
  for j in range(i+1, 410):
    ans += counter[i] * counter[j] * (i - j) * (i - j)
print(ans)
