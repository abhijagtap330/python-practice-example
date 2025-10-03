num = 29

count = 0

if num>1:
    for i in range(1,num+1):
        if(num%i) == 0:
            count=count+1
    if count == 2:
        print("Number is Prime number")
    else:
        print("Number is not Prime number")
        
num = 29
flag = 0
for i in range(2,num):
    if i % 2 == 1:
        flag = 1
if flag == 1:
    print("Not Prime Number")
else:
    print("Prime Number") 
    

n1 = 0
n2 = 1
for i in range(1,10):
    sum = n1+n2
    print(sum)
    n1 = n2
    n2 = sum
    
def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

print(prime_number(29))