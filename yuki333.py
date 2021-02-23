A, B = map(int, input().split())

ans = 0
mx = 2*(10**9)
if A > B:
  #C > A or A > C > B
  ans += mx-A
  ans += A-B-1
else: # A < B
  #C < A or B > C > A
  if A != 1:
    ans += A-1
  ans += B-A-1
print(ans)
