N = int(input())

A = list(map(int, input().split()))
tt = 1
for a in A:
  tt *= a

tt -= 1

ans = 0
for a in A:
  ans += tt%a
  
print(ans)
