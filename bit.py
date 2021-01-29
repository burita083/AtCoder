n = int(input())

l = []
for bit in range(1 << n):
    a = []
    for i in range(n):
        if bit&(1 << i):
            print(bit, i)
            a.append(i)
    l.append(a)
print(l)