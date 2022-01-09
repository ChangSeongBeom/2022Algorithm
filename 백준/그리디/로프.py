import sys

N=int(sys.stdin.readline())
arrList=[]
for _ in range(N):
    tmp=int(sys.stdin.readline())
    arrList.append(tmp)
arrList.sort()
result=-1

for i in range(0,len(arrList)):
    tmp=arrList[i]
    length=len(arrList)-i
    value=tmp*length
    result=max(result,value)
print(result)