#quick sort algorithm
n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i+1} th element: ")))

print(arr)
n=len(arr)

def partition(a,low,high):
    i=low
    j=high
    pivot=a[low]

    while(i<j):
        while a[i]<=pivot and i<high:
            i+=1

        while a[j]>pivot and j>low:
            j-=1

        if i<j:
            a[i],a[j]=a[j],a[i]

    a[low],a[j]=a[j],a[low]
    return j


def quick_sort(a,low,high):
    if low>=high:
        return
    mid=partition(a,low,high)
    quick_sort(a,low,mid-1)
    quick_sort(a,mid+1,high)

quick_sort(arr,0,n-1)
print("sorted array",arr)

        