from re import match
for i in range(int(input())):
    name,mail = input().strip().split()
    if match(r'^<[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$',mail):
        print(name,mail)
