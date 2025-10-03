def remove_duplicate(string):
    unique_char = []
    for i in string:
        if i not in unique_char:
            unique_char += i
    return unique_char

string="Abhijeeeetttttt"
print(remove_duplicate(string))

print(set(string))

