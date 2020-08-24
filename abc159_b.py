def ispalindrome(str): return 1 if str == str[::-1] else 0
a = input()
l = len(a)
left = a[0:(l-1)//2]
right = a[(l-1)//2+1:]
if ispalindrome(left) and ispalindrome(right) and ispalindrome(a):
  print("Yes")
else:
  print("No")
