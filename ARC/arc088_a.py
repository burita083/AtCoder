X, Y = map(int, input().split())

l = [X]

i = X

count = 0
while i*2 <= Y:
  i *= 2
  l.append(i)

print(len(l))
