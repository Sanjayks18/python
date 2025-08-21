n=int(input("enter the number of rows:" ))

for i in range(1,n+1):
    char=97
    breakpoint=(2*i-1)//2
    #space
    for j in range (n-i):
        print(" ",end="")

    #letter
    for j in range (2*i-1):
        print(chr(char),end="")
        if j<breakpoint:
            char+=1
        else:
            char-=1
    print()
    #space

