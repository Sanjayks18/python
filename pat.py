n=int(input("enter the number of rows:" ))

for i in range(n):
    ch=65
    for j in range(n-i):
        print(" ",end="")

    for j in range (2*i+1):
        print(chr(ch),end="")
        if j<i:
            ch+=1
        else:
            ch-=1
        

    print()