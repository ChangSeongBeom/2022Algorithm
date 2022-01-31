import sys

N,find=map(int,sys.stdin.readline().split())
arrList=list(map(int,sys.stdin.readline().split()))


start=0
end=N-1
arrList.sort()
print(arrList)
while start<=end:
    mid=(start+end)//2

    if find==arrList[mid]:
        print(mid+1)
        exit(0)
    else:
        if arrList[mid]<find:
            start=mid+1
        else:
            end=mid-1
