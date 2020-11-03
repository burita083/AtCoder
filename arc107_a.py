A, B, C = map(int, input().split())
MOD = 998244353
sum = A*(A+1)//2 * B*(B+1)//2 * C*(C+1)//2
print(sum % MOD)