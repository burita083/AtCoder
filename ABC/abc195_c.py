N = int(input())

length = len(str(N))
#1,000,000,000,000,000
#1,000 l4
#1,000,000 l7
#1,000,000,000 l10
#1,000,000,000,000 l13
#1,000,000,000,000,000 L16
#1,000,000,000,000,000
#1,077,302,721,373,64
#2,007,182,818,284,590
#2007182818284590

if N <= 999:
  print(0)
  exit()

mx6 = 1000000 -1
m6 = mx6-1000+1

mx9 = 1000000000-1
m9 = 2*(mx9-1000000+1)

mx12 = 1000000000000-1
m12 = 3*(mx12-1000000000+1)

mx15 = 1000000000000000-1
m15 = 4*(mx15-1000000000000+1)
sm = 0
if length <= 6:
  sm += N-1000+1
  #mx6 = 1000000 -1
  #m6 = mx6-1000+1
elif length <= 9:
  sm += m6
  sm += 2*(N-1000000+1)
  #Jmx9 = 1000000000-1
  #m9 = 2*(mx9-1000000+1)
elif length <= 12:
  sm += m6
  sm += m9
  sm += 3*(N-1000000000+1)
  #Jmx12 = 1000000000000-1
  #m12 = 3*mx12-1000000000+1)
elif length <= 15:
  sm += m6
  sm += m9
  sm += m12
  sm += 4*(N-1000000000000+1)
  #mx15 = 1000000000000000-1
  #Jm15 = 4*(mx15-1000000000000+1)
elif length == 16:
  sm += m6
  sm += m9
  sm += m12
  sm += m15
  sm += 5*(N-1000000000000000+1)
print(sm)





