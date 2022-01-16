import sys

N,M=map(int,sys.stdin.readline().split())
result=[]
def dfs(start):
    if len(result)==M:
        for re in result:
            print(re,end=' ')
        print()
        return
    else:
        for i in range(1,N+1):
            result.append(i)
            dfs(start+1)
            result.pop()
dfs(0)