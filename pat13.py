n=int(input("enter the number of rows:"))

for i in range(n):
    for j in range((n-i)):
        print(chr(97+j),end="")
    print()