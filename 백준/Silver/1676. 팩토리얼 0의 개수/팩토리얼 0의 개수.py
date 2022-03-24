facto = 1
for i in range(1,int(input())+1):
    facto *= i
if facto < 10:
    print(0)
facto = str(facto)
for i in range(len(facto)-1,0,-1):
    if facto[i] != '0':
        print(len(facto)-i-1)
        break