triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

h=len(triangle)
dp=[[0]*5 for _ in range(h)]
for r1 in triangle:
    for r2 in r1:
        print(r2,end=' ')
    print('')

dp[0][0]=triangle[0][0]
dp[1][0]=triangle[0][0]+triangle[1][0]
dp[1][1]=triangle[0][0]+dp[1][1]
