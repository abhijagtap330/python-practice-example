def count_of(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    count_v = 0
    count_o = 0
    
    for char in string:
        if char in vowels:
            count_v += 1
        elif char in consonants:
            count_o += 1
    return count_v, count_o
 
vowels_count, consonants_count = count_of("AbhijeetJagtap-1234")
print("Number of vowels:", vowels_count)
print("Number of consonants:", consonants_count)