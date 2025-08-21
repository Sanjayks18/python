n=int(input("enter the number of rows:"))
star=2*(n-2)


for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(star+1):
        print(" ",end="")

    for j in range(i,0,-1):
        print(j,end="")
    print()
    star-=2


