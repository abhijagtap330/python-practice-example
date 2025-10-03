string = "Pythonnnnnnnnnnn"
char = "n"
count = 0

def count_freq(char,string):
    count = 0
    for i in range(len(string)):
        if (string[i] == char):
            count = count + 1
    return count 
            
print(count_freq(char,string))
