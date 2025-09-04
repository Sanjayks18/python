nums=[-2,1,-3,4,-1,2,1,-5,4]
        
maxi=float('-inf')
sum=0
for i in nums:

    sum+=i
    if sum>=maxi:

        maxi=sum
    if sum<0:

        sum=0
    
print(maxi)