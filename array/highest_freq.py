from collections import Counter

def count_freq(list):
    
    count_of_freq = Counter(list)
    
    max_frequency = max(count_of_freq,key=count_of_freq.get)
    
    return max_frequency,count_of_freq

print(count_freq({1,2,3,423,1,21,4,32,12,12,"Abhijeet"}))

print(count_freq([1,2,3,423,1,21,4,32,12,12,"Abhijeet"]))

print(count_freq((1,2,3,423,1,21,4,32,12,12,"Abhijeet")))