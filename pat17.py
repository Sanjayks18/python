n=int(input("enter the number of rows:" ))


for i in range(n):
    for j in range(n-i):
         print("*",end="")

    for j in range(2*i):   
        print(" ",end="")


    for j in range(n-i):
         print("*",end="")
    print()

start=2*n-2
for i in range(1,n+1):
    for j in range(i):
         print("*",end="")

    for j in range(start):   
        print(" ",end="")
        


    for j in range(i):
         print("*",end="")
        
    print()
    start-=2