import sys

T=int(sys.stdin.readline())

def solution(arr,value):

    s=0
    e=len(arr)-1

    while s<=e:
        m=(s+e)//2

        if arr[m]>value:
            s=m+1
        else:
            return s
            e=m-1



for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    arr1=list(map(int,sys.stdin.readline().split()))
    arr2=list(map(int,sys.stdin.readline().split()))
    arr1.sort()
    print(arr1,arr2)
    re=0
    for value in arr2:
        print(solution(arr1,value))
    print(re)
