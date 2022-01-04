import math
def solution(n):
    ans=int(math.sqrt(n))
    if ans*ans==n:
        return (ans+1)*(ans+1)
    else:
        return -1