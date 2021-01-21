m=int(input())
m_val=set(map(int,input().split()))
n=int(input())
n_val=set(map(int,input().split()))
ans=n_val.symmetric_difference(m_val)
for i in sorted(ans):
    print(i)
