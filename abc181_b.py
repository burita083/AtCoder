N = int(input())

ans = 0
for _ in range(N):
  A, B = map(int, input().split())
  b = B*(B+1) //2
  AA = A-1
  a = (AA)*(AA+1) //2
  ans += b-a
    
print(ans)

