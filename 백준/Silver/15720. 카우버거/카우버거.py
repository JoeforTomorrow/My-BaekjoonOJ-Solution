a,b,c = map(int,input().split())
res = 0
burger = list(map(int,input().split()))
side = list(map(int,input().split()))
drink = list(map(int,input().split()))
print(sum(burger)+sum(side)+sum(drink))
for i in range(min(a,b,c)):
    res += (max(burger) + max(side) + max(drink)) * 0.9
    burger.pop(burger.index(max(burger)))
    side.pop(side.index(max(side)))
    drink.pop(drink.index(max(drink)))
res += (sum(burger)+sum(side)+sum(drink))
print(int(res))