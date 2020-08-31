# get String
S = input()

# define dictionary
d = {}
for s in S:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

# print k => v
for k, v in zip(d.keys(), d.values()):
    print(k, v)
    
