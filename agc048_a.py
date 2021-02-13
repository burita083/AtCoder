T = int(input())
atcoder = "atcoder"
lenAtcoder = len(atcoder)
for i in range(T):
  count = 0
  S = input()
  lenS = len(S)
  now = S
  if atcoder < S:
    print(count)
    continue
  else:
    if atcoder == S:
      print("1")
      continue
    else:# atcoder > S
      if lenAtcoder < lenS:
        for i in range(lenAtcoder-1):
          if now[i] < atcoder[i]:
            count += 1
            if S[i+1] > atcoder[i]:
              print(count)
              break
            elif S[i+1] < atcoder[i]:
              print("-1")
              break
            else:
              if i == 0: continue
              now = now[:i] + now[i+1] + now[i] + now[i+1:]
              print(now)
          else:
            if i == 0: continue
            print(now[:i], now[i+1], now[i],now[i+2:], "aaa")
            now = now[:i] + now[i+1] + now[i] + now[i+2:]
            print(now, "aaaaaaaaaaaaa")
      else:
        print("bb")

  

#aab > #ab
#aaab > aaa