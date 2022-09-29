n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

count_freq = [0] * (10 ** 5 + 5)
j = times = 0

for i in range(n):
  if count_freq[a[i]] == 0:
    times +=1
  count_freq[a[i]] += 1

  while times == k:
    count_freq[a[j]] -= 1

    if count_freq[a[j]] ==  0:
      print(j + 1, i + 1)
      exit()
    j += 1

print(-1, -1)