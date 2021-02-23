A,B,C = map(int,input().split())
 
a = A
arr = [a]
for i in range(11):
    a *= A
    if a%10 == arr[0]%10: break
    arr.append(a)
 
k = pow(B,C,len(arr))
if k == 0: k = 4
print(pow(A, k, 10))