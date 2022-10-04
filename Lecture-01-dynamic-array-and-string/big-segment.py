n = int(input())

L = []
R = []

for _ in range(n):
  a, b = list(map(int, input().split()))
  L.append(a)
  R.append(b)

left = min(L)
right = max(R)

for i in range(n):
  if left == L[i] and right == R[i]:
    print(i + 1)
    exit()

print(-1)
