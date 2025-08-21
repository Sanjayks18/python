n=int(input("enter the number of element:"))
arr=[]
for i in range(n):
    x=int(input("enter the elements:"))
    arr.append(x)
print(arr)

for i in range(n-1,0,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
print(arr)