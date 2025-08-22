n=int(input("enter the number of element:"))
arr=[]
for i in range(n):
    x=int(input("enter the elements:"))
    arr.append(x)
print(arr)

for i in range(n):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1

print(arr)