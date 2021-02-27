N = int(input())

point_dict1 = {}
point_dict2 = {}
for i in range(N):
  x, y = map(int, input().split())
  point_dict1[x+y] = (x, y)
  point_dict2[x-y] = (x, y)
min1 = min(point_dict1)
max1 = max(point_dict1)
min2 = min(point_dict2)
max2 = min(point_dict2)

print(max(max1-min1, max2-min2))
