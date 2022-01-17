import sys

N,M=map(int,sys.stdin.readline().split())
result=[]

def chk():
    flag=True
    for i in range(0,len(result)-1):
        if result[i]>=result[i-1]:
            flag=False
    return flag

def dfs(start):
    if len(result)==M:
        if chk()==True:
            print(result)
            return
    for i in range(1,N+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()

dfs(0)