n=int(input("enter the number of element:"))
arr=[]
for i in range(n):
    x=int(input("enter the elements:"))
    arr.append(x)
print(arr)

for i in range(n-1):
    min=i
    for j in range(i,n):
        if arr[min]>arr[j]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]


print(arr)