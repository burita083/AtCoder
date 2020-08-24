N, K = map(int, input().split())
X = list(map(int, input().split()))

time = 100000000000007
for i in range(0, N-K+1):
  if X[i] < 0 and X[i+K-1] > 0:
    if abs(X[i]) >= abs(X[i+K-1]):
      time = min(abs(X[i+K-1]-X[i]) + abs(X[i+K-1]),time)
    else:
      time = min(abs(X[i+K-1]-X[i]) + abs(X[i]),time)
  if X[i] >= 0:
      time = min(abs(X[i+K-1]-X[i]) + abs(X[i]),time)
  if X[i+K-1] <= 0:
      time = min(abs(X[i+K-1]-X[i]) + abs(X[i+K-1]),time)

print(time)