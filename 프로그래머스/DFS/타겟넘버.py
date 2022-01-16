cnt=0
def dfs(sum,depth,numbers,target):
    global cnt
    if depth==len(numbers):
        if sum==target:
            cnt+=1
            return
    else:
        dfs(sum+numbers[depth],depth+1,numbers,target)
        dfs(sum-numbers[depth],depth+1,numbers,target)
def solution(numbers, target):
    dfs(0,0,numbers,target)
    return cnt