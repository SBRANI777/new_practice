#prime number or not
n=int(input("enter any number:"))
Flag=False
for i in range(2,n):
    if n%i==0:
       Flag=True
if Flag:
   print("not a prime number")
else:
    print("prime number")