import sys

N=int(input())
arr1=list(map(int,sys.stdin.readline().split()))

M=int(input())
arr2=list(map(int,input().split()))


arr1.sort()

def binary(arr,value):
    s,e=0,len(arr)-1

    while s<=e:
        m=(s+e)//2

        if arr[m]==value:
            return 1
        elif arr[m]<=value:
            s=m+1
        else:
            e=m-1
    return 0

for value in arr2:
    result = binary(arr1,value)
    print(result)