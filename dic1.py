s2="this is for the code in vs code im code"
words=s2.split()
d1={}
for word  in words:
    if not word in d1:
        d1[word]=1
    else:
        d1[word]+=1
print(d1)