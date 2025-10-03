def replace_string(string, char):
    
    return string.replace("e", char)
    
print(replace_string("Abhijeet", "*"))


def lower_upper(string):
    return string.capitalize()

str1 = "ABHIJEET"
print(lower_upper(str1))


def to_title_case(s):
    return ' '.join(word.capitalize() for word in s.split())

print(to_title_case("Abhijeet JAGTAP"))
