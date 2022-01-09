#https://www.acmicpc.net/problem/1260
import sys
from collections import deque
N,M,V=map(int,sys.stdin.readline().split())
visited=[False]*(N+1)
adj=[[] for _ in range(N+1)]

for _ in range(M):
    src,dst=map(int,sys.stdin.readline().split())
    adj[src].append(dst)
    adj[dst].append(src)

for i in range(N+1):
    adj[i].sort()

def dfs(adj,visited,start):
    if not visited[start]:
        visited[start]=True
        print(start,end=' ')

        for e in adj[start]:
            dfs(adj,visited,e)

def bfs(adj,visited,start):

    queue=deque([start])

    while queue:
        tmp=queue.popleft()
        if not visited[tmp]:
            visited[tmp]=True
            print(tmp,end=' ')

            for e in adj[tmp]:
                if not visited[e]:
                    queue.append(e)
dfs(adj,visited,V)
print()
visited=[False]*(N+1)
bfs(adj,visited,V)