X = int(input())

#x^5-y^5=(x-y)(x^4+x^3y+x^2y^2+xy^3+y^4)

for x in range(1, 300):
  if ((x**5) - ((x-1)**5)) >= 1000000000:
    print(x)

for a in range(0, 121):
  for b in reversed(range(-122, 120)):
    if b**5 == a**5-X:
      print(a, b)
      exit()

