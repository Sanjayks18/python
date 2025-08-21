#hashing count the number of times a element occur in a array

n=int(input("enter the size of array :"))

arr=[]
for i in range(n):
    x=int(input(f" enter {i+1} element:"))
    arr.append(x)
print(arr)

hash=[0]*(max(arr)+1)

for i in range(n):
    hash[arr[i]]+=1

print("hash array",hash)

elements=int(input("enter the number of elements :"))
temp=[]
for i in range(elements):
    x=int(input(f" enter {i+1} element:"))
    temp.append(x)

print("frequent element array",temp)

for q in temp:
    if q<len(hash):
        print(f"{q} occurs {hash[q]} times")
    else:
        print(f"{q} not present in array")