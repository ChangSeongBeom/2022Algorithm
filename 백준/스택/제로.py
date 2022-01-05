import sys

T=int(input())
stack=[]
for _ in range(T):
    tmp=int(input())
    if tmp==0:
        stack.pop()
    else:
        stack.append(tmp)

if not stack:
    print(0)
else:
    print(sum(stack))
