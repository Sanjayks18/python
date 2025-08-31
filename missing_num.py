#find the missing number in an array
arr=[1,2,3,5]
n=len(arr)
sum=(n+1)*(n+2)//(2)
arr_sum=0
for i in arr:
    arr_sum+=i

res=sum-arr_sum
print("the missing number is :",res)