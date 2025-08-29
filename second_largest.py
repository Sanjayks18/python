n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i+1} th element: ")))

print(arr)
n=len(arr)
large=arr[0]
secondlarge=-1
for i in range(n):
    if arr[i]>large:
        secondlarge=large
        large=arr[i]

    

print("the secondlargest element is :",secondlarge)

