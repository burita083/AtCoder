A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

d = abs(A-B)
n = V-W

if n <= 0:
  print("NO")
  exit()
print("YES" if n * T >= d else "NO")