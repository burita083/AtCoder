S = input()

if len(S) < 5:
    print("NO")
    exit()

if len(S) > 9:
    print("NO")
    exit()

if len(S) == 9 and S == "AKIHABARA":
    print("YES")
    exit()

if len(S) == 9 and S != "AKIHABARA":
    print("NO")
    exit()


if S == "AKIHBR" or S == "AKIHABR" or S == "AKIHBRA" or S == "AKIHABAR" or S == "AKIHBARA" or S == "AKIHBRA" or S == "AKIHABRA":
    print("YES")
    exit()

if S == "KIHBR" or S == "KIHABR" or S == "KIHBRA" or S == "KIHABAR" or S == "KIHBARA" or S == "KIHBRA" or S == "KIHABRA" or S == "KIHABARA":
    print("YES")
    exit()
print("NO")






