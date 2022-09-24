n = int(input())

while n != 0:
  car = list(map(int, input().split()))
  car = car[::-1]

  stack = []
  result = 'yes'
  current_order = 1

  while (len(car) > 0 or len(stack) > 0) and result == 'yes':
    if len(car) > 0 and car[-1] == current_order:
      current_order += 1
      car.pop()
    elif len(stack) > 0 and stack[-1] == current_order:
      stack.pop()
      current_order += 1
    else:
      if len(car) > 0:
        stack.append(car.pop())
      else:
        result = 'no'

  print(result)
  n = int(input())