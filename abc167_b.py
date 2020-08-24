A, B, C, K = map(int, input().split())

if A >= K:
  print(K)
  exit()
else:
  K -= A
  if B >= K:
    print(A)
    exit()
  else:
    K -= B
    if K <= C:
      A -= 1*K
    
print(A)

