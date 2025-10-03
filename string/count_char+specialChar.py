string = input("Enter a string: ")

alpha = 0
digit = 0
special_char = 0

for i in string:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else:
        special_char += 1
print("alphabets =",alpha,"digits =",digit,"specialChars =",special_char)
