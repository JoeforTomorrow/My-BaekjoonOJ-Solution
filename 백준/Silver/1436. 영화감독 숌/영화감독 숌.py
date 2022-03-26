a=int(input())
lst=[ i for i in range(1000*a) if '666' in str(i)]
print(lst[a-1])