x = float(input())
y = float(input())
quad = x*y

if quad > 0:
  if x >= 0:
    print(1)
  else:
    print(3)
elif quad < 0:
  if x >= 0:
    print(4)
  else:
    print(2)