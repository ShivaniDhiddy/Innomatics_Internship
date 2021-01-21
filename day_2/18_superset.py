A = set(input().split())
B=[set(input().split()) for i in range(int(input()))]
ans=all(map(lambda x: (A > x),B ))
print(ans)
