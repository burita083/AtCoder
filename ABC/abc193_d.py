from collections import Counter
K = int(input())

S = input()[:4]
T = input()[:4]
cnt = [K] * 10
for c in S:
    cnt[int(c)] -= 1
for c in T:
    cnt[int(c)] -= 1

ans = 0
s = "111139"
print(s.count("1"), "aaaaaaaaaaaaaaaaa")
print(s.count("3"), "aaaaaaaaaaaaaaaaa")
print(s.count("9"), "aaaaaaaaaaaaaaaaa")
print(s.count("2"), "aaaaaaaaaaaaaaaaa")
def score(S):
    cnt = [0] * 10
    for c in S:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10 ** S.count(str(i))
    return ans

for i in range(1, 10):
  print((S+str(i)).count(str(i)))
  print(cnt[i], "aajkjh")
  if cnt[i] <= 0:continue

  for j in range(1, 10):
    if i == j: continue
    if cnt[j] <= 0:continue

    if score(S+str(i)) > score(T + str(j)):
      ans += cnt[i] * cnt[j]

for i in range(1, 10):
  if cnt[i] < 2:
    continue
  if score(S+str(i)) > score(T + str(i)):
    ans += cnt[i] * (cnt[i]-1)
card = 9*K
remain = card - 8
print(ans/remain/(remain-1))



