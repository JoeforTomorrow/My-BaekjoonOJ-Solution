import sys

todo = {'Re':0, 'Pt':0, 'Cc':0, 'Ea':0, 'Tb':0, 'Cm':0, 'Ex':0}

cnt = 0
lines = sys.stdin.readlines()
# lines = input()
for line in lines:
    jobs = list(line.split())
    for job in jobs:
        if job in todo.keys():
            todo[job] = todo.get(job, 0) + 1
        cnt += 1

for job in todo:
    print(job, todo.get(job), '{:.2f}'.format(todo.get(job)/cnt))
    
print('Total', cnt, '1.00')