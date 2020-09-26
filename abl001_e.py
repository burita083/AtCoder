N, Q = map(int, input().split())

S = ""
mod = 998244353
  
for _ in range(N):
  S += "1"

for _ in range(Q):
  L, R, D = map(int, input().split())
  pre = S[:L-1]
  middle = S[L-1:R]
  after = S[R:]
  str_list = list(middle)
  for i in range(len(middle)):
    str_list[i] = str(D)
  middle = "".join(str_list)
  S = str((int(pre)%mod+int(middle)%mod+int(after)%mod))%mod)
  print(S)
