n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i+1} th element: ")))

print(arr)
n=len(arr)

j=-1
for i in range(n):
    if arr[i]==0:
        j=i
        break

for i in range(j+1,n):
    if arr[i]!=0:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1

print("after moving zero",arr)