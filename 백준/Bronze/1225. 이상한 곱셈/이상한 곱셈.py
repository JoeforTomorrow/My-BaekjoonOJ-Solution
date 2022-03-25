a, b = input().split()
an = [ int(a[i]) for i in range(len(a)) ]
bn = [ int(b[i]) for i in range(len(b)) ]
print(sum(an)*sum(bn))