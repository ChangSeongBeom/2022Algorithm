# https://www.acmicpc.net/problem/2667
import sys

N=int(sys.stdin.readline())
arrList=[list(map(int,input())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]


dx=[-1,0,1,0]
dy=[0,-1,0,1]
result=[]
def dfs(y,x):
    if not visited[y][x]:
        visited[y][x]=True

        for i in range(0,4):
            tmpy=y+dy[i]
            tmpx=x+dx[i]

            if tmpy<0 or tmpx<0 or tmpy>N-1 or tmpx>N-1:
                continue
            if not visited[tmpy][tmpx] and arrList[tmpy][tmpx]==1:
                result[len(result)-1]+=1
                dfs(tmpy,tmpx)


for i in range(len(arrList)):
    for j in range(0,len(arrList[i])):
        if arrList[i][j]==1 and not visited[i][j]:
            result.append(1)
            dfs(i,j)
result.sort()
print(len(result))
for re in result:
    print(re)