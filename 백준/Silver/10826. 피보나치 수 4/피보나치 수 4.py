i = 0
j = 1
k = 1

n = int(input()) + 1

while k != n:
    i = i + j
    j = i - j
    k = k + 1

print(i)