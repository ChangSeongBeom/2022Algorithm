#https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    tmp=s.split(' ')
    re=[]
    for tmpp in tmp:
        for i in range(0,len(tmpp)):
            if i%2==0:
                re.append(tmpp[i].upper())
            else:
                re.append(tmpp[i].lower())
        re.append(' ')
    print(re)
    re.pop()
    return(''.join(re))