import re
n= int(input())

pattern = '^[4-6]{1}[0-9]{3}([-]{0,1}[0-9]{4}){3}$'
pattern_rep = '(\d)\1{3,16}'

for i in range(n):
   a = input().strip()
   b = ''.join(a.split('-'))
   c = re.compile(pattern)
   d = re.compile(pattern_rep)
   r= None
   r = c.match(a)
   r2 = re.search(r'(\d)\1{3,}',b)
   if r== None or r2 != None:
       print('Invalid')
   else:
       print('Valid')
