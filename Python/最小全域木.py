class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self._size = [1] * N
        self.count = 0

    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)

    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self._size[ra] < self._size[rb]: ra,rb = rb,ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1

    def size(self,a):
        return self._size[self.root(a)]

N, M = map(int, input().split())
graph = []

for _ in range(M):
  a, b, w = map(int, input().split())
  graph.append((w, a-1, b-1))

graph.sort()
uf = UnionFind(N)
ans = 0
for (w, now, to) in graph:
  if uf.is_same(now, to) == False:
    uf.unite(now, to)
    ans += w
print(ans)