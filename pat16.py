n=int(input("enter the number of rows:" ))
for i in range(1,n+1):
    start=101
    for j in range(start-i,start-n,start-i):
        print(chr(start),end="")
        
    
    print()

