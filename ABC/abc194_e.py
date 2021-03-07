N, M = map(int,input().split())
A = list(map(int,input().split()))

ct = [0]*(N+1) #区間内に存在する個数をカウント
# 最初の区間[0:M]について
for i in range(M):
  ct[A[i]] += 1

for i in range(N+1):
  if ct[i] == 0:
    ans = i
    break

# 区間を1ずつシフトする
# 考え方：
# 　シフトするごとに、左端の値が飛び出し、右端の値が入るイメージ。
# 　ある数xが常に区間に含まれるなら、その数が飛び出してくることはないか、飛び出した時に区間内に他のxが存在するかのいずれか。
print(ct, "start")
for i in range(N-M):
  ct[A[i]] -= 1 # A[i]が外れる
  ct[A[i+M]] += 1 # A[i+M]が入る
  print(ct, i)
  if ct[A[i]] == 0:
    print(ct, "aaa", i)
    # A[i]が区間内に存在しないときに限り、A[i]をmexの最小値の候補とすべき。
    ans = min(A[i], ans)
    
print(ans)