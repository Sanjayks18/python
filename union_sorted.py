#union of sorted array
n = int(input("Enter size of array1: "))
arr1 = [int(input(f"enter{i+1} element:")) for i in range(n)]
arr2 = [int(input(f"enter{i+1} element:")) for i in range(n)]

def sorted_union(ar1,ar2):
    res=[]
    i,j=0,0
    while i<len(ar1) and j<len(ar2):
        if ar1[i]<ar2[j]:
            if not res or res[-1]!=ar1[i]:
                res.append(ar1[i])
            i+=1

        elif ar1[i]>ar2[j]:
            if not res or res[-1]!=ar1[j]:
                res.append(ar2[j])
            j+=1


        else:#arr[i]==arr[j]
            if ar1[i]==ar2[j]:
                if not res or res[-1]!=ar1[i]:
                    res.append(ar1[i])
                i+=1
                j+=1

    while(i<len(ar1)):
        res.append(ar1[i])
        i+=1

    while(j<len(ar2)):
        res.append(ar2[j])
        j+=1
    return res

x=sorted_union(arr1,arr2)
print(x)


