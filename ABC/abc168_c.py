N = int(input())
s = str(N)

if s[-1] == "3":
  print("bon")
elif s[-1] == "0" or s[-1] == "1" or s[-1] == "6" or s[-1] == "8":
  print("pon")
else:
  print("hon")
