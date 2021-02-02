n = int(input())

d = {}
for index, i in enumerate(range(0, 161, 40)):
  for j in range(1, 21):
    d[i+j] = j

for index, i in enumerate(range(20, 181, 40)):
  for index, j in enumerate(reversed(range(1, 21))):
    d[i+index+1] = j

print(d[n])