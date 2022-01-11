import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())

arrList=[]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
visited=[[False]*M for _ in range(N)]

for _ in range(N):
    tmp=list(map(int,sys.stdin.readline().rstrip()))
    arrList.append(tmp)


queue=deque([(0,0)])

while queue:
    tmpy,tmpx=queue.popleft()
    visited[tmpy][tmpx]=True

    for i in range(4):
        tmpyy=tmpy+dy[i]
        tmpyx=tmpx+dx[i]

        if tmpyy<0 or tmpyx<0 or tmpyy>N-1 or tmpyx>M-1:
            continue

        if not visited[tmpyy][tmpyx] and arrList[tmpyy][tmpyx]==1:
            arrList[tmpyy][tmpyx]=arrList[tmpy][tmpx]+1
            queue.append((tmpyy,tmpyx))
print(arrList[N-1][M-1])
