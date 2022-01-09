import sys

N,K=map(int,sys.stdin.readline().split())
coinList=[]
cnt=0

for _ in range(N):
    tmp=int(sys.stdin.readline())
    coinList.append(tmp)

coinList=sorted(coinList,reverse=True)

for i in range(0,len(coinList)):
    if K>=coinList[i]:
        cnt+=K//coinList[i]
        K-= coinList[i] * (K//coinList[i])

print(cnt)