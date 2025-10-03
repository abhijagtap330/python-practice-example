arr = [0, 1, 2, 0, 3, 0, 4]

def last_zero(array):
    
    list1 = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[list1], array[i] = array[list1], array[i]
            list1 +=1 
            
    return array

print(last_zero(arr))