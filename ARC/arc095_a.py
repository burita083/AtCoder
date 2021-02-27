N = int(input())

"1 2 3 4 5を配列に"
X = list(map(int, input().split()))
sx = sorted(X)

left = sx[len(sx)//2-1]
right = sx[len(sx)//2]
print(left, right)
for x in X:
  if x <= left:
    print(right)
  else:
    print(left)