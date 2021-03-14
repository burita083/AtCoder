import copy
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
"nの約数列挙"
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass
N = int(input())

X = list(map(int, input().split()))
X.sort()

dpp = [False] * 51
dp = [False] * 51

ans = 1
mn = float('inf')

if all(i % 2 == 0 for i in X):
  print(2)
  exit()

if all(i % 3 == 0 for i in X):
  print(3)
  exit()

if all(i % 5 == 0 for i in X):
  print(5)
  exit()

if all(i % 7 == 0 for i in X):
  print(7)
  exit()

if N == 2:
  if X[0] % 2 == 0 and X[1] % 2 == 0:
    ans = 2
    mn = min(mn, ans)
  elif X[0] % 3 == 0 and X[1] % 3 == 0:
    ans = 3
    mn = min(mn, ans)
  elif X[0] % 5 == 0 and X[1] % 5 == 0:
    ans = 5
    mn = min(mn, ans)
  elif X[0] % 7 == 0 and X[1] % 7 == 0:
    ans = 7
    mn = min(mn, ans)
  else:
    for x in X:
      if x % 2 == 0 and dp[x] == False:
        ans *= 2
        x = 2
        while x <= 50:
          dp[x] = True
          x += 2
        continue

      if x % 3 == 0 and dp[x] == False:
        ans *= 3
        x = 3
        while x <= 50:
          dp[x] = True
          x += 3
        continue


      if x % 5 == 0 and dp[x] == False:
        ans *= 5
        x = 5
        while x <= 50:
          dp[x] = True
          x += 5
        continue

      if x % 7 == 0 and dp[x] == False:
        ans *= 7
        x = 7
        while x <= 50:
          dp[x] = True
          x += 7
        continue

      if dp[x] == False:
        ans *= x
        while x <= 50:
          dp[x] = True
          x += x
        continue
    mn = min(mn, ans)
else:
  for x in X:
    if x % 2 == 0 and dp[x] == False:
      ans *= 2
      x = 2
      while x <= 50:
        dp[x] = True
        x += 2
      continue

    if x % 3 == 0 and dp[x] == False:
      ans *= 3
      x = 3
      while x <= 50:
        dp[x] = True
        x += 3
      continue


    if x % 5 == 0 and dp[x] == False:
      ans *= 5
      x = 5
      while x <= 50:
        dp[x] = True
        x += 5
      continue

    if x % 7 == 0 and dp[x] == False:
      ans *= 7
      x = 7
      while x <= 50:
        dp[x] = True
        x += 7
      continue

    if dp[x] == False:
      ans *= x
      while x <= 50:
        dp[x] = True
        x += x
      continue
  mn = min(mn, ans)

  ans = 1
  dp = copy.deepcopy(dpp)
  for x in X:
    if x % 3 == 0 and dp[x] == False:
      ans *= 3
      x = 3
      while x <= 50:
        dp[x] = True
        x += 3
      continue

    if x % 2 == 0 and dp[x] == False:
      ans *= 2
      x = 2
      while x <= 50:
        dp[x] = True
        x += 2
      continue

    if x % 5 == 0 and dp[x] == False:
      ans *= 5
      x = 5
      while x <= 50:
        dp[x] = True
        x += 5
      continue

    if x % 7 == 0 and dp[x] == False:
      ans *= 7
      x = 7
      while x <= 50:
        dp[x] = True
        x += 7
      continue

    if dp[x] == False:
      ans *= x
      while x <= 50:
        dp[x] = True
        x += x
      continue
  mn = min(mn, ans)

  ans = 1
  dp = copy.deepcopy(dpp)
  for x in X:
    if x % 5 == 0 and dp[x] == False:
      ans *= 5
      x = 5
      while x <= 50:
        dp[x] = True
        x += 5
      continue
      
    if x % 2 == 0 and dp[x] == False:
      ans *= 2
      x = 2
      while x <= 50:
        dp[x] = True
        x += 2
      continue

    if x % 3 == 0 and dp[x] == False:
      ans *= 3
      x = 3
      while x <= 50:
        dp[x] = True
        x += 3
      continue

    if x % 7 == 0 and dp[x] == False:
      ans *= 7
      x = 7
      while x <= 50:
        dp[x] = True
        x += 7
      continue

    if dp[x] == False:
      ans *= x
      while x <= 50:
        dp[x] = True
        x += x
      continue
  mn = min(mn, ans)
  
  ans = 1
  dp = copy.deepcopy(dpp)
  for x in X:
    if x % 7 == 0 and dp[x] == False:
      ans *= 7
      x = 7
      while x <= 50:
        dp[x] = True
        x += 7
      continue
          
    if x % 2 == 0 and dp[x] == False:
      ans *= 2
      x = 2
      while x <= 50:
        dp[x] = True
        x += 2
      continue

    if x % 3 == 0 and dp[x] == False:
      ans *= 3
      x = 3
      while x <= 50:
        dp[x] = True
        x += 3
      continue

    if x % 5 == 0 and dp[x] == False:
      ans *= 5
      x = 5
      while x <= 50:
        dp[x] = True
        x += 5
      continue

    if dp[x] == False:
      ans *= x
      while x <= 50:
        dp[x] = True
        x += x
      continue
  mn = min(mn, ans)
print(mn)
  

  