import sys

N,M=map(int,sys.stdin.readline().split())
result=[]
visited=[False]*(N+1)

def dfs(start,depth):
    if depth==M:
        for i in result:
            print(i,end=' ')
        print('')
        return

    for i in range(1,N+1):
        if not visited[i]:
            result.append(i)
            visited[i]=True
            dfs(i,depth+1)
            visited[i]=False
            result.pop()

dfs(0,0)

