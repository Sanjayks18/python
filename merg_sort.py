n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i+1} th element: ")))

print(arr)
n=len(arr)


def mergsort(arr,low,high):
    if low==high:
        return
    
    mid=(low+high)//2

    mergsort(arr,low,mid)
    mergsort(arr,mid+1,high)
    merg(arr,low,mid,high)



def merg(arr,low,mid,high):
    temp=[]
    l=low
    r=mid+1
    while(l<=mid and r<=high):
        if(arr[l]<=arr[r]):
            temp.append(arr[l])
            l+=1

        else:
            temp.append(arr[r])
            r+=1


    while(l<=mid):
        temp.append(arr[l])
        l+=1
    while(r<high):
        temp.append(arr[r])
        r+=1

 
    for i in range(len(temp)):
        arr[low + i] = temp[i]

res=mergsort(arr,0,n-1)
print("sorted array",arr)