def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

S = input()
if is_int(S):
  print((int(S)*2))
else:
  print("error")