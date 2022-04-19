import re
import sys
input = sys.stdin.readline
for i in range(int(input())):
    txt=input()
    if re.match("[A-F]{0,1}A+F+C+[A-F]{0,1}$",txt):
        print("Infected!")
    else:
        print("Good")
