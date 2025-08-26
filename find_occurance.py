arr = [1, 2, 2, 2, 3, 4, 5]
x = 2

first = -1
last = -1

for i in range(len(arr)):
    if arr[i] == x:
        if first == -1:
            first = i
        last = i

print("First:", first)
print("Last:", last)