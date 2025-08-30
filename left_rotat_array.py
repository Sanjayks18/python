#rotat left a array of d elements
n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i+1} th element: ")))

d=int(input("enter D(number of elements to be rotat):"))
d=d%n
print(arr)
n=len(arr)

temp=arr[:d]
#shifting
for i in range(d,n):
    arr[i-d]=arr[i]
#addback at end
for i in range(n-d,n):
    arr[i]=temp[i-(n-d)]

print("rotated array ",arr)

    
