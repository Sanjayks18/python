n=int(input("enter the number of rows:" ))
space=2*n-2

for i in range(1,2*n):
    stars=i 
    if i>n:
        stars=2*n-i
    for j in range(1,stars):
        print("*",end="")


    for j in range(1,space):
        print(" ",end="")

    for j in range(1,stars):
        print("*",end="")
    if i<n:
        space-=2
    else:
        space+=2
    print()
