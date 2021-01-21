from collections import Counter
k=int(input())
inp=list(input().split())
ans=dict(Counter(inp))
for i in ans:
    if ans[i]==1:
        print(i)
