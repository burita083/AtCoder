"nの約数列挙"
def divisor(n):
    ans = 0
    for i in range(1,int(n**0.5)+1):
      if i == 1:
        ans += 3
      else:
        if n%i == 0:
          if i**2 == n or i ** 3 == n or i ** 4  == n or i ** 5 == n or i ** 6 == n:
            print(n, "aaaaaaaa", i)
            ans += 3
            if i**2 != n:
              ans += 6
            continue
          ans += 6
    return ans
K = int(input())


count = 0
for i in range(1, K+1):
  if i == 1:
    count += 1
  else:
    temp = divisor(i)
    print(temp, i)
    count += temp
print(count)


