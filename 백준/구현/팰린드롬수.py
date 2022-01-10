import sys

while True:
    N=int(sys.stdin.readline())
    if N==0:
        break
    arrList=str(N)
    reversedList=list(reversed(arrList))

    reversedList=''.join(reversedList)

    if arrList==reversedList:
        print("yes")
    else:
        print("no")