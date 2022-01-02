nums=[1,2,7,6,4]
tmp=[]
cnt=0
def isPrime(number):
    cc=0
    for i in range(1,number+1):
        if number% i ==0:
            cc+=1
    if cc==2:
        return True
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            tmp.append(nums[i]+nums[j]+nums[k])

for tmpValue in tmp:
    if isPrime(tmpValue):
        cnt+=1
print(cnt)