N, K = map(int, input().split())

"1 2 3 4 5を配列に"
A = list(map(int, input().split()))
A.sort()
count = A.count(A[0])
remain = len(A) - count
if remain % (K-1) == 0:
  print(remain//(K-1))
else:
  print((remain//(K-1))+1)