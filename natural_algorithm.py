x = float(input('Enter Number: '))
n = int(input('Enter Number: '))

sample = 1
for i in range(1,n+1):
    term = (x-1//x) ** i
    sample += term
    
print(sample)





    