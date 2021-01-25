# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=list(map(int,input().split()))
str=".|."
for i in range(1,n,2):
    print((str*i).center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,0,-2):
    print((str*i).center(m,"-"))
