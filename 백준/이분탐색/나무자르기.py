import sys

N,M=map(int,sys.stdin.readline().split())

arrList=list(map(int,sys.stdin.readline().split()))

lt=1
rt=max(arrList)
result=0

def Count(len):
    cnt=0

    for value in arrList:
        if value>=len:
            cnt+=value-len
    return cnt
while lt<=rt:
    mid=(lt+rt)//2
    res=Count(mid)


    if res>=M:
        lt=mid+1
        result = mid
    else:
        rt=mid-1
print(result)