def cnt_two(n):
    t = 0
    while n != 0:
        n //= 2
        t += n
    return t

def cnt_fiv(n):
    f = 0
    while n != 0:
        n //= 5
        f += n
    return f

n,m = map(int,input().split())

print(min(cnt_two(n)-cnt_two(n-m)-cnt_two(m),cnt_fiv(n)-cnt_fiv(n-m)-cnt_fiv(m)))