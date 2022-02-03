import sys

N,M=map(int,sys.stdin.readline().split())
arrList=[]
for _ in range(N):
    tmp=int(sys.stdin.readline())
    arrList.append(tmp)

arrList.sort()

lt=1
rt=max(arrList)

maxValue=-1
res=0

while lt<=rt:
    cnt=0
    mid=(lt+rt)//2

    for x in arrList:
        cnt+=x//mid

    if cnt>=M :
        lt=mid+1

    else:
        rt=mid-1
print(rt)