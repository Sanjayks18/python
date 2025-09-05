#extraction of digits
import math
def f1():
        n=int(input("enter the digit: "))

        while n>0:
            digit=n%10
            print(digit)
            n=n//10

#f1()

def f2():
      n=int(input("enter the digit: "))
      count=0
      while n>0:
            count+=1
            n=n//10
      print(count)f2()

def f3():
      n=int(input("enter the digit: "))
      last=0
      while n>0:
            ld=n%10
            n=n//10
            last=(last*10)+ld
            
      print(last)
#f3()


def f4():
      n=int(input("enter the number: "))
      fact=[]

      for i in range(1,int(math.sqrt(n)+1)):
            if n%i ==0:
                  fact.append(i)
                  if(n//i!=i):
                        fact.append(n//i)
      fact.sort()
      print(fact)
#f4()

def f5():
      n=int(input("enter the number: "))
      count=0

      for i in range(1,int(math.sqrt(n)+1)):
            if n%i ==0:
                  count+=1
                  if(n//i!=i):
                        count+=1
      if count==2:
            print("it is prime number")
      else:
            print("it is  not a prime number")
            

     

f5()