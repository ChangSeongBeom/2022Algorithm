import sys

N,M=map(int,sys.stdin.readline().split())
result=[]

def dfs(start):
    if len(result)==M:
        print(result)
    else:
        for i in range(start,N+1):
            result.append(i)
            dfs(start+1)
            result.pop()
dfs(1)
