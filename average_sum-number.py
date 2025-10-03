sum = 0
count = 0

while True:
    
    number = float(input("..........Number.........."))
    
    if number == 0:
        break
    
    sum += number
    count += 1

if count > 0:
    average = sum / count
    
    print(average)
    print(sum)