# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
m_val=set(map(int,input().split()))
b=int(input())
n_val=set(map(int,input().split()))
ans=len(n_val.intersection(m_val))
print(ans)
