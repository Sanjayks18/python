#longedt subarray with sum k

arr=[1,2,3,1,1,1,4,2,3]
n=len(arr)
target=3
lent=0
for i in range (0,n):
    s=0
    for j in range(i,n):
        s+=arr[j]
        if s==target:
            lent=max(lent,(j-i)+1)

print("completed",lent)