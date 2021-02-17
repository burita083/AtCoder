S = input()

s = ""
for i in range(0, 7):
    s += S[i]

if s == "keyence":
    print("YES")
    exit()

s = ""
for i in range(1, 8):
    s = S[-i] + s

if s == "keyence":
    print("YES")
    exit()

if S[0] != "k" and S[-1] != "e":
    print("NO")
    exit()

s = ""
if S[0] == "k" and S[1] != "e":
    for i in range(1, 7):
        s = S[-i] + s
    if s == "eyence":
        print("YES")
        exit()
    else:
        print("NO")
        exit()

s = ""
if S[0] == "k" and S[1] == "e" and S[2] != "y":
    for i in range(1, 6):
        s = S[-i] + s
    if s == "yence":
        print("YES")
        exit()
    else:
        print("NO")
        exit()
s = ""
if S[0] == "k" and S[1] == "e" and S[2] == "y" and S[3] != "e":
    for i in range(1, 5):
        s = S[-i] + s
    if s == "ence":
        print("YES")
        exit()
    else:
        print("NO")
        exit()

s = ""
if S[0] == "k" and S[1] == "e" and S[2] == "y" and S[3] == "e" and S[4] != "n":
    for i in range(1, 4):
        s = S[-i] + s
    if s == "nce":
        print("YES")
        exit()
    else:
        print("NO")
        exit()
    
s = ""
if S[0] == "k" and S[1] == "e" and S[2] == "y" and S[3] == "e" and S[4] == "n" and S[5] != "c":
    for i in range(1, 3):
        s = S[-i] + s
    if s == "ce":
        print("YES")
        exit()
    else:
        print("NO")
        exit()
s = ""
if S[0] == "k" and S[1] == "e" and S[2] == "y" and S[3] == "e" and S[4] == "n" and S[5] == "c" and S[6] != "e":
    for i in range(1, 2):
        s = S[-i] + s
    if s == "e":
        print("YES")
        exit()
    else:
        print("NO")
        exit()
print("NO")