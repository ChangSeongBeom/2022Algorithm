import sys
sys.setrecursionlimit(10**6)
M,N,K=map(int,sys.stdin.readline().split())

arrList=[]
dy=[0,-1,0,1]
dx=[-1,0,1,0]
result=[]
visited=[[False] * N for _ in range(M)]
for _ in range(M):
    tmpList=[0]*N
    arrList.append(tmpList)
for _ in range(K):
    a,b,c,d=map(int,sys.stdin.readline().split())
    for i in range(b,d):
        for j in range(a,c):
            arrList[i][j]+=1

def dfs(y,x):
    visited[y][x]=True

    for i in range(4):
        tmpy=y+dy[i]
        tmpx=x+dx[i]

        if tmpy<0 or tmpx<0 or tmpy>M-1 or tmpx>N-1:
            continue
        if arrList[tmpy][tmpx]==0 and not visited[tmpy][tmpx]:
            result[len(result)-1]+=1
            dfs(tmpy,tmpx)

for i in range(0,len(arrList)):
    for j in range(0,len(arrList[i])):
        if arrList[i][j]==0 and not visited[i][j]:
            result.append(1)
            dfs(i,j)
print(len(result))
result.sort()
for re in result:
    print(re,end=' ')