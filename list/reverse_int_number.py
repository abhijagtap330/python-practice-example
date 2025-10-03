num = "1234"

def reverse_numbers(num):
    string_number = str(num)
    reverse = string_number[::-1]
    return int(reverse)

print(reverse_numbers(num))

reversed_s = ""
for i in range(len(num) -1, -1, -1):
    reversed_s += num[i]
    

    