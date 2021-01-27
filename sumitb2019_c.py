X = int(input())

count = X//100
mx = count*100+(5*count)
print(mx)
if X<=int(mx):
    print(1)
else:
    print(0)
