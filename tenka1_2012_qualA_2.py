S = input()
A = S.split(' ')
print(A)
B = [a for a in A if a != '']
print(B)
print(','.join(B))