n=int(input("enter the number of rows:"))

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
            print("*",end="")
    for l in range(n-i-1):
                print(" ",end="")
    print()       
