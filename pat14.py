n=int(input("enter the number of rows:"))


for i in range(n):
    for j in range(i):
        print(chr(97+i),end="")
    print()