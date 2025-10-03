
def count_freq(number):
    frequency = {}
    for i in number:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

list1 = [12,12,12,22,21,334,4,56,6767,67,7,87,85,34,53,2,3]
print(count_freq(list1))


# num = 15
# flag = 0
# for i in range(2,num):
#   if num%i==0:
#     flag = 1
#     break
# if flag == 1:
#   print('Not Prime')
# else:
#   print("Prime")