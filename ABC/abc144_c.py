N = int(input())

"nの約数列挙"
def divisor(n):
  ans = float('inf')
  for i in range(1,int(n**0.5)+1):
      if n%i == 0:
          x = i
          y = n//i
          ans = min((x-1)+(y-1), ans)
  return ans
ans = divisor(N)
if ans == float('inf'):
  print("0")
  exit()
print(divisor(N))