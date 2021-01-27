 #Enter your code here. Read input from STDIN. Print output to STDOUT
S=input()
import re
m = re.search(r'([A-Za-z0-9])\1+',S)
if m:
    print m.group(1)
else:
    print -1
