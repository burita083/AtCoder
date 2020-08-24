from itertools import accumulate
A=[1,4,3,4,6,5]
S = list(accumulate(A))
print(S)
print(S[2] - S[0])