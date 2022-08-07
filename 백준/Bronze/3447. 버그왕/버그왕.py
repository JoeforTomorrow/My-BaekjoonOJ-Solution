import sys 
import re
txt = sys.stdin.readlines()
for i in txt:     
    while True:
        result=re.sub('BUG','',i)         
        if 'BUG' in result: i= result
        else: 
            print(result,end="") 
            break