A, B, N = map(int, input().split())

mx = -1
count = 0
for x in range(1, N+1):
  temp = ((A*x) // B) - A*(x//B)
  mx = max(mx, temp)
  count +=1
  if count == 300000000:
    break

print(mx)