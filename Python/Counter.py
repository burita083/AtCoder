import collections
N = int(input())

l = []
for x in range(N):
  s = input()
  l.append(s)

c = collections.Counter(l)

print(len(c))

st = set(C.keys())
s1, s2, s3 = set(C.keys()) #数がわかってれば出せる
ln = len(C)
e = C[0] #なければゼロあれば、Value
