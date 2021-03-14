import random

a = int(input())

test = ""
for i in range(a): 
  test += str(random.randrange(50)) + " "

print(test)
