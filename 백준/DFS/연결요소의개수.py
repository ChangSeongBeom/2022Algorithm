import sys
sys.setrecursionlimit(10**6)
N,M=map(int,sys.stdin.readline().split())
visited=[False]*(N+1)
adj=[[] for _ in range(N+1)]
cnt=0
for _ in range(M):
    src,dst=map(int,sys.stdin.readline().split())
    adj[src].append(dst)
    adj[dst].append(src)


def dfs(start):
    visited[start]=True

    for e in adj[start]:
        if not visited[e]:
            dfs(e)
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)