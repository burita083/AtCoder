A, K = map(int, input().split())

next = A+ 1+A*K
diff = next-A
start = A
if A == 0 and K == 0:
    print(2*10**12)
    exit()
if K == 0:
    print(2*10**12-A)
    exit()
    
for i in range(10**6):
    start += diff*((K+1)**i)
    if start >= 2*10**12:
        print(i+1)
        exit()
