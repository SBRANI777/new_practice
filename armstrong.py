n=int(input("enter any number:"))
temp=n
rev=0
while(n>0):
    r=n%10
    rev=rev+(r**3)
    n=n//10
if rev==temp:
    print("armstrong")
else:
    print("not a arm strong")