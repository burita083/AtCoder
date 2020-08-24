a = int(input())
b = int(input())

"1 2 3 4 5を配列に"
A = list(map(int, input().split()))

s = list(input())
for ss in s:
  print(ss)

"文字列"
S = input()
print(S[0])

"1 2 3 4 5 を配列に入れる"
li = input().split()
for l in li:
  print(l)

 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
n = a-b
print(n)

"切り下げた整数"
q = 10 // 3
mod = 10 % 3
print(q, mod)
# 3 1

a = 0.364364
print(a) #0.364364
print("{:.6f}".format(a)) #0.364364
print("{:.4f}".format(a)) #0.3644 小数点第4位に丸めることもできる。

"変数をそれぞれに分ける"
c, d, e = map(int, input().split())
 
n = c+d+e

"配列"
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
for num in list1:
  print(num)

"0から4"
for number in range(5):
    print(number)

 
if n==17:
  print('YES')
  
else:
  print('NO')


number = 0
print ("start")
while number < 5:
    print(number)
    number += 1
print ("end")
 
"left = a[0:(l-1)//2]"
"right = a[(l-1)//2+1:"