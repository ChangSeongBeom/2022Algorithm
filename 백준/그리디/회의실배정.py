import sys

N=int(sys.stdin.readline())
meeting=[]
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    meeting.append((a,b))

meeting.sort(key=lambda x:(x[1],x[0]))

cnt=0
endTime=0
for s,e in meeting:
    if s>=endTime:
        endTime=e
        cnt+=1
print(cnt)


