numbers=[1,1,1,1,1]
target=3
cnt=0

def dfs(numbers,target,idx,sum):
    global cnt
    length=len(numbers)

    if length==idx:
        if target==sum:
            cnt+=1
            return
    else:
        dfs(numbers,target,idx+1,sum-numbers[idx])
        dfs(numbers,target,idx+1,sum+numbers[idx])

def solution(numbers,target,idx,sum):
    global cnt
    dfs(numbers,target,0,0)
    print(cnt)
solution(numbers,target,0,0)