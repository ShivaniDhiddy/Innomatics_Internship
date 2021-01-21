if __name__ == '__main__':
    data=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
check=sorted(set([j for i,j in data]))[1]
ans=[i for i,j in data if j==check]
for i in sorted(ans):
    print(i)
