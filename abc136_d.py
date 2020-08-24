S = input()
N = len(S)
left_R = [0] * N
right_L = [N-1] * N

for i, s in enumerate(S[1:], 1):
  left_R[i] = i if s == 'R' else left_R[i-1]

for i, s in enumerate(S[N-2::-1], 1):
  i = N-1-i
  right_L[i] = i if s == 'L' else right_L[i+1]

answer = [0] * N
for i, (s, R, L) in enumerate(zip(S, left_R, right_L)):
  if s == 'L':
    j = left_R[i]
    if (i+j) & 1:
      j += 1
  else:
    j = right_L[i]
    if (i+j) & 1:
      j -= 1
  answer[j] += 1
print(' '.join(map(str, answer)))
  