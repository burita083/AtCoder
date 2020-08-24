import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

data = np.fromstring(read(), np.int64, sep =' ')

N, K = data[:2]
P = np.hstack([[0], data[2:] + 1])

Pcum = P.cumsum()
x = Pcum[K:] - Pcum[0:-K]
print(x.max()/2)