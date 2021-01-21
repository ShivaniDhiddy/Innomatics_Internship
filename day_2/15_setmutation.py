# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
A = set(map(int,input().split()))
for i in range(int(input())):
    s, b = input().split()
    B=set(map(int,input().split()))
    if s == 'intersection_update':
        A &= B
    elif s == 'update':
        A |= B
    elif s == 'symmetric_difference_update':
        A ^= B
    else:
        A -= B
print(sum(A))
