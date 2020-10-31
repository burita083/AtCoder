A, B, C = map(int, input().split())
amari = 998244353
a = A*(A+1)%amari
b = B*(B+1)%amari
c = C*(C+1)%amari
a *= 0.5
b *= 0.5
c *= 0.5
print(a)
print(b)
print(c)
print(int(a*b*c)%amari)

sum = A*(A+1)//2 * B*(B+1)//2 * C*(C+1)//2
print(sum % 998244353)