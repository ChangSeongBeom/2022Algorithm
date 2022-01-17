# n=3
# computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n=3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

cnt=0

def dfs(start,visited,adj):
     visited[start]=True

     for e in adj[start]:
         if not visited[e]:
             dfs(e,visited,adj)



def solution(n, computers):
    global cnt
    visited=[False]*(n)
    adj=[[] for _ in range(len(computers))]
    for i in range(0,len(computers)):
        for j in range(0,len(computers[i])):
            if computers[i][j]==1:
                adj[i].append(j)
    for i in range(0,len(computers)):
        if not visited[i]:
            cnt+=1
            dfs(i,visited,adj)
solution(n,computers)
print(cnt)