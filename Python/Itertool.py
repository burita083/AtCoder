import itertools
N = int(input())
ans = 0


#repeatは桁数
for i in range(1, 10):
  for x in itertools.product("753", repeat=i):
    s= ''.join(x)
    if int(s) > N: continue
    if '3' not in s: continue
    if '5' not in s: continue
    if '7' not in s: continue
    ans += 1
print(ans)


#ABC150_C
N = int(input())

P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

l = []
for i in range(N):
  l.append(i+1)
a = 0
b = 0
for index, ptn in enumerate(list(itertools.permutations(l, N))):
  if ptn == P:
    a = index+1

  if ptn == Q:
    b = index+1
print(abs(a-b))


#順列・重複あり
all = itertools.product('abc', repeat=2)
for x in all:
    print(x)


('a', 'a')
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'b')
('b', 'c')
('c', 'a')
('c', 'b')
('c', 'c')

#組合せ・重複あり
all = itertools.combinations_with_replacement('abc', 2)
for x in all:
    print(x)


('a', 'a')
('a', 'b')
('a', 'c')
('b', 'b')
('b', 'c')
('c', 'c')


#組合せ・重複なし
all = itertools.combinations('abc', 2)
for x in all:
    print(x)


('a', 'b')
('a', 'c')
('b', 'c')