def f1():


    num=[1,2,3,4,5,6,7,8,9,10]

    print(num[2])
    print(num[-1])
    print(num[2:5])
#f1()

def f2():
    num=[]
    num.append(1)
    num.append(2)
    num.append(3)
    num.append(4)
    num.append(5)
    num.append(6)
    print(num)
    num.pop()
    print(num)
#f2()
def f3():
    num=[10,20,30,40,50]
    print(num)
    num.insert(2,90)
    print("after insert")
    print(num)
    num.remove(40)
    print("after remove")
    print(num)
#f3()

def f4():
    num=[7,5,9,3,8,4,1,2,6,3,5]
    print("before sorting")
    print(num)
    num.sort()
    print("after  sorting")
    print(num)

    num.reverse()
    print("reversing")
    print(num)
#f4()

def f5():
     num=[1,2,3,4,5,6,7,8,9,10]
     num1=[7,5,9,3,8,4,1,2,6,3,5]

     num1.extend(num)
     print(num1)

f5()