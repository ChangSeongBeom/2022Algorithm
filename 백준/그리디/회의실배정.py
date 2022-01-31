import sys

N=int(sys.stdin.readline())
meeting=[]
for _ in range(N):
    src,dst=map(int,sys.stdin.readline().split())
    meeting.append((src,dst))

meeting.sort(key=lambda x:(x[1],x[0]))

for s,e in meeting:
    print(s,e)