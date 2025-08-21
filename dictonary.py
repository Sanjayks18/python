def f1():
    student={"name": "sanjay","age": 20,"grade":"a+"}
    print(student["name"])
    print(student.get("grade"))
    print(student.get("roolno", "not found"))
    print(student.keys())
    print(student.values())

    for key in student:
        print(key, student.get(key))

#f1()

def f2():
    dic={}
    dic["a"]=1
    dic["b"]=2
    dic["c"]=3
    dic["d"]=4
    print(dic)
    dic["b"]=99
    print(dic)
#f2()

def f3():
    dic={}
    dic["a"]=1
    dic["b"]=2
    dic["c"]=3
    dic["d"]=4
    dic.pop("c")
    print(dic)
    dic.popitem()
    print(dic)

#f3()

def f4():
    nums = [4, 6, 4, 7, 4, 6, 7, 7, 7]
    count={}

    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    print(count)
#f4()

def f5():
    d={1:"a",2:"b",3:"c",4:"d"}
    print("dictionary items ")
    print(d)
    print("after performing pop")

    d.pop(2)
    print(d)
    print("after performing pop item ")
    d.popitem()
    print(d)
#f5()

def f6():
    nums = [1, 3, 2, 1, 4, 1, 3, 2, 3]

    dic={}
    for num in nums:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    print("The most number time repeated is:")
    
f6()