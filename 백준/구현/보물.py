from itertools import permutations
import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))

AList=sorted(A,reverse=True)
BList=sorted(B)


minValue=0
for i in range(0,len(AList)):
    minValue+=AList[i]*BList[i]
print(minValue)
