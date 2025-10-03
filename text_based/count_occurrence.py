text = 'This is my own desk. Now I need to know who are you?'

def count_occ(text):
    split = text.split()
    count = {}
    for i in split:
        
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    return count

print(count_occ(text)) 