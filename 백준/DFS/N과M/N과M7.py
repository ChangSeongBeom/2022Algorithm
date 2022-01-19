import sys

N,M=map(int,sys.stdin.readline().split())
arrList=list(map(int,sys.stdin.readline().split()))
arrList.sort()
result=[]



def dfs(idx):
    if len(result)==M:
        for re in result:
            print(re,end=' ')
        print()
        return
    else:

        for i in range(0,N):
            result.append(arrList[i])
            dfs(i)
            result.pop()


dfs(0)