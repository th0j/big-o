n = int(input())

for j in range(n):
  t = input()

  stack = []
  count = 0
  max_count = 0

  for i in range(len(t)):
    if t[i] == '<':
      stack.append(t[i])
    else:
      if len(stack) > 0:
        stack.pop()
        count += 1
      else:
        break
      # update max_count after pop from stack
      if len(stack) == 0:
        max_count = count

  print(max_count * 2)