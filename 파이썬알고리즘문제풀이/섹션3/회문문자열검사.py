import sys

N=int(sys.stdin.readline())
arrList=[]
for _ in range(N):
    tmp=sys.stdin.readline().lower().rstrip()
    arrList.append(tmp)


for i in range(0,len(arrList)):
    reversedvalue=''.join(list(reversed(arrList[i])))
    if arrList[i]==reversedvalue:
        print("#%d YES"%(i+1))
    else:
        print("#%d NO"%(i+1))
