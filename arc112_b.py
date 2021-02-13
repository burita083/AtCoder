B, C = map(int, input().split())

ans = 1
if C == 1:
  if B != 0:
    ans += 1 #もとのかずマイナス
elif C == 2:
  if B != 0:
    ans += 1 #もとのかずマイナス
  ans += 1
else:
  if B != 0:
    ans += 1 #もとのかずマイナス
  if C % 2 == 0:
    ans += (C//2-1)*2+1
  else:
    ans += (C//2)*2
  
  if B != 0:
    if (C-1) % 2 == 0:
      ans += ((C-1)//2-1)*2+1
    else:
      ans += ((C-1)//2)*2

print(ans)

