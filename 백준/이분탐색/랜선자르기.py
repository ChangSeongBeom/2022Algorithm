import sys

N,M=map(int,sys.stdin.readline().split())
arrList=[]
for _ in range(N):
    tmp=int(sys.stdin.readline())
    arrList.append(tmp)

arrList.sort()
testList=[i for i in range(arrList[0]+1)]
start=0
end=len(testList)

while start<=end:
    mid=(start+end)//2

    if mid==