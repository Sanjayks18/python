#hashing: count the number of times a letter occur in a string contain only of lower case letters

s=input("enter string: ")
print(s)

hash=[0]*(26)

for i in range(len(s)):
    hash[ord(s[i])-ord('a')]+=1


print("hash array",hash)

elements=int(input("enter the number of characters :"))
temp=[]
for i in range(elements):
    x=(input(f" enter {i+1} element:"))
    temp.append(x)

print("frequent element array",temp)

for ch in temp:
        idx = ord(ch) - ord('a')   # convert character → index (0–25)
        if 0 <= idx < 26:
            print(f"{ch} occurs {hash[idx]} times")
        else:
            print(f"{ch} not present in array")