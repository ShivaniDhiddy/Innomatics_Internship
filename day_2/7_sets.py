def average(array):
    # your code goes here
    avg=sum(set(arr))/len(set(arr))
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
