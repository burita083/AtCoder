import itertools
N = int(input())
S = input()
R = S.count('R')
G = S.count('G')
B = N-R-G
ans = R*G*B

#二重ループの書き方は迷わないようにする
for i in range(N-2):
  for j in range(i+1, N-1):
    k = j + (j-i) # i, j, kのの隙間が全部同じ
    if k >= N:
      break
    if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
      ans -= 1
print(ans)
