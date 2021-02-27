a = int(input())
 
ans = 0
for x in range(a):
  ans += (10000 * (x+1))/a
 
print(ans)