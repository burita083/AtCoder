N = int(input())

aokiSum = 0
cities = []
for x in range(N):
    aoki, takahashi = map(int, input().split())
    aokiSum += aoki
    score = takahashi + aoki + aoki
    cities.append(score)
cities.sort()
cities.reverse()

print(cities)
count = 0
for score in cities:
  count += 1
  aokiSum -= score
  if aokiSum < 0:
    break
print(count)