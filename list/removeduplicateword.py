mylist=["Abhijeet","Jagtap","Abhijeet","Abhijeet","Abhijeet"]

word="Abhijeet"
n=3

count=0
for i in range(0,len(mylist)-1):
    if(mylist[i]==word):
        count=count+1
        if (count==n):
            del mylist[i]
print("Updated list:",mylist)

