x, y, r = map(int, input().split())

left = -1.0-x
top = 1.0+y
right = 1.0+x
bottom = -1.0-y

cellnum = 200

celllen = ( right - left ) / ( cellnum - 1 )

# 円周率πの計算のメイン
# 円内の座標の個数を初期化
in_num = 0

celly = top
for y in range(cellnum):
  cellx = left
  for x in range(cellnum):
    l2 = cellx * cellx + celly * celly
    if 1.0 >= l2:
      in_num += 1
      cellx += celllen
print(in_num)
