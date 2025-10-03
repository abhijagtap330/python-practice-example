#approch1: Temporary Variable
mylist=[12,33,54,21,40]
# size=len(mylist)
#
# tem=mylist[0]
# mylist[0]=mylist[-1]
# mylist[-1]=tem
#
# print(mylist)

#approach2:

mylist[0],mylist[-1]=mylist[-1],mylist[0]

print("List after swapping:",mylist)
