from collections import Counter

def higest_freq(string):
    
    frequency = Counter(string)
    
    max_frequency = max(frequency, key=frequency.get)
    
    return max_frequency 
    
print(higest_freq("Abhijeet"))

