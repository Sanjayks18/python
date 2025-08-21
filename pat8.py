n=int(input("enter n value: "))


for i in range(2*n):
    star=i
    if i>n:
        star=2*n-i
    for j in range(star):
        print("*",end="")    
    print()