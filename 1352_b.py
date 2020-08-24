import itertools
t = int(input())

print(1000000000//9)
#for _ in range(t):
  #odd = []
  #even = []
  #found = False
  #n, k = map(int, input().split())
  #for x in range(1, n+1, 2):
    #odd.append(x)

  #for x in range(2, n+1, 2):
    #even.append(x)

  #comb = list(itertools.combinations_with_replacement(odd, k))
  #for x in comb:
    #if sum(x) == n:
      #print("YES")
      #print(' '.join(map(str, x)))
      #found = True
      #break

  #if found == False:
    #comb = list(itertools.combinations_with_replacement(even, k))
    #for x in comb:
      #if sum(x) == n:
        #print("YES")
        #print(' '.join(map(str, x)))
        #found = True
        #break

  #if found == False:
    #print("NO")