n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    que,*val=input().split()
    if "remove" in que:
        s.remove(int(val[0]))
    elif "discard" in que:
        s.discard(int(val[0]))
    else:
        s.pop()
print(sum(list(s)))
