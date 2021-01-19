N = int(input())

AB = [0] * 1000007
for i in range(N):
  a, b = map(int, input().split())
  AB[a] += 1
  AB[b+1] -= 1

ans = []
a = 0
for ab in AB:
  a += ab
  ans.append(a)
print(max(ans))
