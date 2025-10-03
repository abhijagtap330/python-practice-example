text = "This is my   own   desk!"

def remove_space(text):
    a = text.split()
    return ' '.join(text.split())

print(remove_space(text))


import re

def normalize_text(text): 
    a = re.sub(r'[^a-zA-Z]', '', text)
    return ' '.join(a)

print(normalize_text(text))