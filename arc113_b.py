A, B, C = map(int, input().split())
mod = 10 ** 9+7
if A % mod == 0:
    print(0, 0)
    exit()

y = pow(A, pow(B, C, mod - 1), mod)
Y = str(y)
print(Y[-1])