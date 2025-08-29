n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i+1} th element: ")))

print(arr)
n=len(arr)
small=arr[0]
for i in range(n):
    if arr[i]<small:
        small=arr[i]

print("the small element is :",small)

