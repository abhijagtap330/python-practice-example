# s = input("Write a sentence: ")
# d={"UPPER CASE":0, "LOWER CASE":0}

# for i in s:
#     if i == i.upper():
#         d['UPPER CASE'] += 1
#     elif i == i.lower():
#         d['LOWER CASE'] += 1
#     else:
#         pass

# print("UPPER CASE", d["UPPER CASE"])
# print("LOWER CASE", d["LOWER CASE"])


def compute_value(a):
    
    num_str = str(a)
    
    aa = int(num_str * 2)
    aaa = int(num_str * 3)
    aaaa = int(num_str * 4)
    
    results = a+aa+aaa+aaaa
    
    return results

# Input from the user
input_value = int(input("Enter a digit: "))
output = compute_value(input_value)

# Print the result
print(output)


tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if i%2==0:
		li.append(i)

tp2=tuple(li)
print (tp2)

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i

# print(d)
    
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))
