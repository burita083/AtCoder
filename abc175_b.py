N = int(input())

L = list(map(int, input().split()))

count = 0
for i in range(0, N-2):
  for j in range(1, N-1):
    if L[i] == L[j]:
      continue
    for k in range(2, N):

      if i < j and j < k:
        if L[i] == L[k]:
          continue

        if L[j] == L[k]:
          continue

        if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
          count += 1

print(count)