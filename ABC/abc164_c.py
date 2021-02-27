import collections
N = int(input())

l = []
for x in range(N):
  s = input()
  l.append(s)

c = collections.Counter(l)
s = collections.Counter("aaabbbbbcc")

print(c)
print(len(c))
print(s)

print(c.items())
print(c.most_common(2))