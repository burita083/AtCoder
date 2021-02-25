N = int(input())

A = list(map(int, input().split()))

flags = [1] * N
count = 1
oneorhundred = 0
for index, a in enumerate(A):
  if a == 100 or a == 1:
    oneorhundred += 1
    continue

  if a % 2 == 0:
    count *= 2

sm = (3**(N-oneorhundred)) * (2**oneorhundred)
print(sm-count)
