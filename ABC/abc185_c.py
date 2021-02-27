from scipy.special import comb

L = int(input())
ans = comb(L-1, 11, exact=True)
print(ans)