#find freequency of each element in a list
list1=[2,3,3,4,4,5,2,4]
list2=[]
count=0
for i in list1:
    if not i in list2:
        list2.append(i)
        count=1
    else:
        count=count+1
   
print(list2)