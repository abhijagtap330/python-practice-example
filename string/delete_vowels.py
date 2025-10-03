def delete_vowels(string):
    vowels = "aeiouAEIOU"
    without_vowels = "-".join([i for i in string if i not in vowels]) # c for c in str if c not in vowels
    return without_vowels

print(delete_vowels("end of the day"))