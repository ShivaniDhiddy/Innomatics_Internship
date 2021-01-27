# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input().strip())):
    valid = True
    id = input().strip()
    if re.match(r'[a-zA-Z0-9]{10}', id) == None:
        valid = False
    elif re.search(r'([a-zA-Z0-9]{1}).*\1{1}', id) != None:
        valid = False
    elif re.search(r'[0-9]{1}.*[0-9]{1}.*[0-9]{1}', id) == None:
        valid = False
    elif re.search(r'[A-Z]{1}.*[A-Z]{1}', id) == None:
        valid = False
    if valid:
        print("Valid")
    else:
        print("Invalid")
