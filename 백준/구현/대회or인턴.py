import sys

N,M,K=map(int,sys.stdin.readline().split())

cnt=0
total=N+M

if N>=(M*2):
    cnt+=M
else:
    cnt=N//2
remain=total-(cnt)*3

if remain>=K:
    print(cnt)
else:
    tmp=0
    K=K-remain
    for i in range(1,cnt+1):
        if i*3>=K:
            tmp=i
            break
    cnt-=tmp
    print(cnt)
