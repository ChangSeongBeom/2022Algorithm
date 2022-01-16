import sys

tmpList = []
result = []
visited = [False] * (9)
for _ in range(9):
    tmp = int(sys.stdin.readline())
    tmpList.append(tmp)


def dfs(start, sum):
    if sum == 100 and len(result) == 7:
        result.sort()
        for re in result:
            print(re)

    for i in range(0, len(tmpList)):
        if not visited[i]:
            result.append(tmpList[i])
            visited[i] = True
            dfs(i, sum + tmpList[i])
            visited[i] = False
            result.pop()


dfs(0, 0)