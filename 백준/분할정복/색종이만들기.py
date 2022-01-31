import sys

N=int(sys.stdin.readline())
arrList=[]

blue=0
white=0

for _ in range(N):
    tmp=list(map(int,sys.stdin.readline().split()))
    arrList.append(tmp)

def dfs(y,x,arrList,N):
    default_color=arrList[y][x]
    global blue,white

    for i in range(y,y+N):
        for j in range(x,x+N):
            if arrList[i][j]!=default_color:
                dfs(y,x,arrList,N//2)
                dfs(y, x+N//2, arrList, N // 2)
                dfs(y+N//2, x, arrList, N // 2)
                dfs(y+N//2, x+N//2, arrList, N // 2)
                return
    if default_color:
        blue+=1
    else:
        white+=1

dfs(0,0,arrList,N)
print(blue,white)