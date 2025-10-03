def replace_vowels(string):
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            string = string.replace(char,"---")
            break
    return string
string = "Hello World"

print(replace_vowels(string=string))
