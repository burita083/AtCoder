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

#uf = UnionFind(N)
#for a,b in AB:
    #a,b = a-1,b-1
    #if uf.is_same(a,b): continue
    #uf.unite(a,b)

#ans = 0
#for i in range(N):
    #ans = max(ans, uf.size(i))

N = int(input())


ans = 1
for i in range(2, N):
  ans += 1/i
ans *= N
print(ans)

 