#https://programmers.co.kr/learn/courses/30/lessons/42586

progresses=[93, 30, 55]
speeds=[1,30,5]
result=[]

def solution(progresses, speeds):
    while progresses:
        for i in range(0,len(progresses)):
            progresses[i]+=speeds[i]

        cnt=0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1


        if cnt>0:
            print(cnt)
            result.append(cnt)
solution(progresses,speeds)