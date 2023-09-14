def average(array):
       s = set(array)
       return sum(s)/len(s)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = arr[0:n]
    result = average(arr1)
    print(result)

