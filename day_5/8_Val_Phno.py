# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    if re.match('^[7-9][0-9]{9}$', input()):
        print("YES")
    else:
        print('NO')
