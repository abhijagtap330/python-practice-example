string = 'abhijeetrew323edwed' #'abhijeetjagtap330@gmail.com'

spl = string.split('@')[0]
print(spl)

def delete_elements(string,re):
    
    remove_elements = string.replace(re,"")
    
    return remove_elements

re='e'
print(delete_elements(string,re))

result = ''
for char in string:
    if char != re:
        result += char

print(result)