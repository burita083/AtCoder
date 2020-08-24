w, h = map(int, input().split())
ans = ""

if (w % 4 == 0 and h % 3 == 0) : 
  ans = "4:3" 

if (w % 16 == 0 and h % 9 == 0) : 
  ans = "16:9" 

if (w == 4 and h == 3) :
  ans = "4:3" 

if (w == 16 and h == 9) :
  ans = "16:9" 

print(ans)