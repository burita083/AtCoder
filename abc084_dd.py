def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

Q = int(input())
N = 10**5+1
cums = [0] * N
a = 0
for i in range(1, N):
    if is_prime(i):
        if is_prime((i+1)//2):
            a += 1
            cums[i] = a
            continue
        cums[i] = a
        continue
    cums[i] = a
    continue


ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    if r-l == 0:
        if is_prime(l):
            if is_prime((l+1)//2):
                ans.append(1)
                continue
            ans.append(0)
            continue
        ans.append(0)
        continue
    else:
        count = cums[r] - cums[l-1]
        ans.append(count)

for a in ans:
    print(a)