N = int(input())

C = input()

if N % 2 == 0:
  mid = N//2
else:
  mid = N//2+1

Rcount = C.count("R")
rcount = C.count("R", 0, Rcount)
print(Rcount-rcount)