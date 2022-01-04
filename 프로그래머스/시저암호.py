#https://programmers.co.kr/learn/courses/30/lessons/12926

s=" . x z"
n=5
re=[]


def solution(s, n):
    for sValue in s:
        if sValue.isalpha():
            if ord(sValue) >= ord('a') and ord(sValue) <= ord('z'):
                if ord(sValue) + n > ord('z'):
                    re.append(chr(ord('a') + (ord(sValue) + n - ord('z'))-1))
                else:
                    re.append(chr(ord(sValue) + n))
            elif ord(sValue) >= ord('A') and ord(sValue) <= ord('Z'):
                if ord(sValue) + n > ord('Z'):
                    re.append(chr(ord('A') + (ord(sValue) + n - ord('Z'))-1))
                else:
                    re.append(chr(ord(sValue) + n))
        else:
             re.append(sValue)

    print(''.join(re))
solution(s,n)
