import re
s = ""
for i in range(int(input())):
    s += input()  + '\n'

s = re.sub('(?<= )\&\&(?= )', 'and', s)
s = re.sub('(?<= )\|\|(?= )', 'or', s)
print(s)
