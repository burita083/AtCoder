S = input()
if len(S)==1:
    print('Yes' if S=='8' else 'No')
    exit()
if len(S)==2:
    for n in range(16,99,8):
        s = str(n)
        if s==S or s[::-1]==S:
            print('Yes')
            exit()
    print('No')
    exit()

from collections import Counter
c = Counter(S)
print(c)

for n in range(0,999,8):
    s = str(n).zfill(3)
    c2 = Counter(s)
    if c&c2 == c2:
        print('Yes')
        exit()
print('No')