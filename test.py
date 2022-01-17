N, M = map(int, input().split())
lst = []

def dfs(start):
    if len(lst) == M:  # 탈출 조건
        print(' '.join(map(str, lst)))
        return

    for i in range(start, N+1):
            lst.append(i)
            dfs(i+1)
            lst.pop()
dfs(1)