import sys

N,M=map(int,sys.stdin.readline().split())
arrList=list(map(int,sys.stdin.readline().split()))
arrList.sort()
result=[]
visited=[False]*(N)
def dfs(idx):
    if len(result)==M:
        for re in result:
            print(re,end=' ')
        print()
        return
    else:

        for i in range(0,N):
            if not visited[i]:
                visited[i]=True
                result.append(arrList[i])
                dfs(i+1)
                visited[i]=False
                result.pop()


dfs(0)