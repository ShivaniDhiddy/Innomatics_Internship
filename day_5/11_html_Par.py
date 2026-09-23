import re
s = "".join([input() for _ in range(int(input()))])

for i in re.finditer(r"<!--.*?-->|(<.*?>)", s):
    a = i.group(1)
    if not a:
        continue
    i = re.match(r"< *(\/?) *(\w+) *(.*?) *(\/?) *>", a)
    if i:
        if i.group(1) == "/":
            print("End   : " + i.group(2))
        else:
            if i.group(4) == "/":
                print("Empty : " + i.group(2))
            else:
                print("Start : " + i.group(2))
            for j in re.finditer(r"([^\s=]+)(?: *= *['\"](.+?)['\"])?", i.group(3)):
                if j.group(2):
                    print("-> %s > %s" % (j.group(1), j.group(2)))
                else:
                    print("-> %s > None" % (j.group(1),))
