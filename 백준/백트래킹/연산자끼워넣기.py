# import sys
#
# N=int(sys.stdin.readline())
#
# arrList=list(map(int,sys.stdin.readline().split()))
# math=list(map(int,sys.stdin.readline().split()))
#
# maxinum=-1e9
# mininum=1e9
#
# def dfs(depth,total,plus,minus,multiply,divide):
#     global maxinum, mininum
#     if depth==N:
#         maxinum=max(maxinum,total)
#         mininum=min(mininum,total)
#         return
#
#     if plus:
#         dfs(depth+1,total+arrList[depth],plus-1,minus,multiply,divide)
#     if minus:
#         dfs(depth+1,total-arrList[depth],plus,minus-1,multiply,divide)
#     if multiply:
#         dfs(depth+1,total*arrList[depth],plus,minus,multiply-1,divide)
#     if divide:
#         dfs(depth+1,int(total/arrList[depth]),plus,minus,multiply,divide-1)
#
#
#
# dfs(1,arrList[0],math[0],math[1],math[2],math[3])
# print(maxinum,mininum)
#



import sys

N=int(sys.stdin.readline())
arrList=list(map(int,sys.stdin.readline().split()))
math=list(map(int,sys.stdin.readline().split()))
maxnum=-1e9
minnum=1e9
def dfs(depth,sum,plus,minus,multiply,divide):
    global maxnum
    global minnum
    if depth==N:
        maxnum=max(sum,maxnum)
        minnum=min(sum,minnum)
    else:
        if plus:
            dfs(depth+1,sum+arrList[depth],plus-1,minus,multiply,divide)
        if minus:
            dfs(depth+1,sum-arrList[depth],plus,minus-1,multiply,divide)
        if multiply:
            dfs(depth+1,sum*arrList[depth],plus,minus,multiply-1,divide)
        if divide:
            dfs(depth+1,int(sum/arrList[depth]),plus,minus,multiply,divide-1)
dfs(1,arrList[0],math[0],math[1],math[2],math[3])

print(maxnum)
print(minnum)