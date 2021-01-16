from collections import Counter
from collections import OrderedDict

N, K = map(int, input().split())

"1 2 3 4 5を配列に"
A = list(map(int, input().split()))
A.sort()
main = []
sub = []
d = {}
od = OrderedDict()
for a in A:
  if a in od:
    od[a] += 1
  else:
    od[a] = 1

#for i, a in enumerate(A):

ans = 0
for kk in range(K):
  main = []
  for i, (k, v) in enumerate(od.items()):
    if v == 0: 
      break
    if i == k:
      main.append(i)
      od[i] -= 1
    else: break
  if len(main) >= 1:
    ans += main[-1] + 1
print(ans)

#print(od)
#main2 = []
#for i, (k, v) in enumerate(od.items()):
  #if v == 0: 
    #break
  #if i == k:
    #main2.append(i)
    #od[i] -= 1

#ans = 0
#print(main)
#print(main2)
#print(od)
#if len(main) >= 1:
  #ans += main[-1] + 1

#if len(main2) >= 1:
  #ans += main2[-1] + 1
#print(ans)