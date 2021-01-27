# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pat= re.compile("(#[a-fA-F\d]{6}|#[a-fA-F\d]{3});*")
for i in range(int(input())):
    line = input()
    if line.startswith("#"):
        continue

    for match in re.findall(pat,line):
        print(match)
