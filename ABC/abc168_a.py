import math
A, B, H, M = map(int, input().split())

start = 30*H
start -= 5.5*M
if start >=180:
  start = 360-start

syahen = A**2 + B**2 - 2*A*B*math.cos(math.radians(start))
print(math.sqrt(syahen))
