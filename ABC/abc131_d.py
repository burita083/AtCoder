N = int(input())

lst = []
for i in range(N):
  N, K = map(int, input().split())
  lst.append((N, K))

lst.sort(key=lambda tup: tup[1])
time = 0
for x in lst:
  time += x[0]
  if time > x[1]:
    print("No")
    exit()

print("Yes")
