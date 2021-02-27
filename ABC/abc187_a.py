A, B = map(int, input().split())

"1 2 3 4 5を配列に"
a = str(A)
b = str(B)
ansA = 0
ansB = 0
for i in a:
  ansA += int(i)

for i in b:
  ansB += int(i)

if ansA >= ansB:
  print(ansA)
else:
  print(ansB)