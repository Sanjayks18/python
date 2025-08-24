sentence=input("enter the sentence: ")

words=sentence.split()

freq={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
for key,value in freq.items():
    print(f"\"{key}\" appears-----> {value}times")
