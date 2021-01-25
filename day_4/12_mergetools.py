def merge_the_tools(string, k):
    # your code goes here
    n=int(len(string)/k)
    for i in range(0, len(string)):
        t=string[i* k : (i + 1) * k]
        ans=""
        for i in t:
            if i not in ans:
                ans+=i
        print(ans)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
