if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        que,*val=input().lower().split()
        value=list(map(int,val))
        #print(que,value)
        if "append" in que:
            lst.append(value[0])
        elif "insert" in que:
            lst.insert(value[0],value[1])
        elif "print" in que:
            print(lst)
        elif "reverse" in que:
            lst.reverse()
        elif "remove" in que:
            lst.remove(value[0])
        elif 'pop' in que:
            lst.pop()
        elif "sort"in que:
            lst.sort()
