import re
z =''.join([i*2 for i in input()])
lst = [x.group(2) for x in re.finditer(r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1})([AEIOUaeiou]{4,})([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1})',z)]
if len(lst) > 0:
    for j in lst :
        s = ''.join([j[i] for i in range(0,len(j),2)])
        print(s)
else :
    print(-1)
