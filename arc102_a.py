N, K = map(int, input().split())

k = 0
while k <= N:
  k += K
"1 2 3 4 5を配列に"
A = list(map(int, input().split()))

for x in A:
  print(x)

"文字列を一文字ずつ入れる"
s = list(input())
print(s)
for ss in s:
  print(ss)

"文字列をいれる。そのままforで回せる"
S = input()
print(S[0])
for s in S:
  print(s)

"a b c を配列に入れる"
li = input().split()
for l in li:
  print(l)

