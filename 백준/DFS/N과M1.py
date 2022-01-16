import sys

N,M=map(int,sys.stdin.readline().split())

visited=[False]*(N+1)
result=[]
def dfs(depth,visited):
    if depth==M:
        for i in result:
            print(i,end=' ')
        print()
    else:
        for i in range(1,N+1):
            if not visited[i]:
                visited[i]=True
                result.append(i)
                dfs(depth+1,visited)
                result.pop()
                visited[i]=False
dfs(0,visited)