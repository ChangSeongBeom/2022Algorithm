import sys

weight=int(sys.stdin.readline())
arrList=[5,3]


maximum=weight//5


for i in range(1,maximum+1):
    if weight>i*5:
        weight-i*5
        