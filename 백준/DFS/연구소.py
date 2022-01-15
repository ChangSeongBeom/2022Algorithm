import sys
from itertools import combinations
h,w=map(int,sys.stdin.readline().split())
arrList=[]
safeList=[]
dy=[0,-1,0,1]
dx=[-1,0,1,0]
maxValue=-1e9
for _ in range(h):
    tmp=list(map(int,sys.stdin.readline().split()))
    arrList.append(tmp)

for i in range(0,len(arrList)):
    for j in range(0,len(arrList[0])):
        if arrList[i][j]==0:
           safeList.append((i,j))

safepermuList=list(combinations(safeList,3))


def dfs(y,x,copyList,visited):
    print(copyList)
    if not visited[y][x]:
        visited[y][x]=1
    for i in range(4):
        tmpy=y+dy[i]
        tmpx=x+dx[i]

        if tmpy<0 or tmpx<0 or tmpy>h-1 or tmpx>x-1:
            continue
        if not visited[tmpy][tmpx] and copyList[tmpy][tmpx]==0:
            copyList[tmpy][tmpx]=2
            dfs(tmpy,tmpx,copyList,visited)
    return copyList

def countVirus(arr):
    cnt=0

    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j]==0:
                cnt+=1
    return cnt

for i in range(0,len(safepermuList)):
    copyList=arrList
    visited=[[False]* w for _ in range(h)]

    copyList[safepermuList[i][0][0]][safepermuList[i][0][1]]=1
    copyList[safepermuList[i][1][0]][safepermuList[i][1][1]]=1
    copyList[safepermuList[i][2][0]][safepermuList[i][2][1]]=1


    print(copyList)
    for j in range(0,len(copyList)):
        for k in range(0,len(copyList[j])):
            if not visited[j][k] and copyList[j][k]==2:
                result=dfs(j,k,copyList,visited)
                countVirusValue=countVirus(result)
                maxValue=max(maxValue,countVirusValue)

print(maxValue)

