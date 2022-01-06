import sys

tmp=input()
stack=[]
re=[]
for i in range(0,len(tmp)):
    if tmp[i]=='<':
        re.append(''.join(stack))
        stack.clear()
        stack.append(tmp[i])
    elif tmp[i]=='>':
        stack.append(tmp[i])
        re.append(''.join(stack))
        stack.clear()
    else:
        if stack:
            re.apend(tmp[i])
        else:
            
print(''.join(re))