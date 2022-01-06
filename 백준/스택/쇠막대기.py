import sys

tmp=input()
stack=[]
res=0
for i in range(0,len(tmp)):
    if tmp[i]=='(':
        stack.append('(')
    else:
        if tmp[i-1]=='(':
            stack.pop()
            res+=len(stack)
        else:
            stack.pop()
            res+=1
print(res)
