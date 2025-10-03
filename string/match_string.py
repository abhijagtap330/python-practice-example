def match_string(str1):
    # Count occurrences of 'cat' and 'hat'
    cat_count = str1.count('cat')
    hat_count = str1.count('hat')

    # Return True if both counts are equal, otherwise False
    return cat_count == hat_count

# Test example
str1 = "bazihatngacat"
print(match_string(str1))  # Output: True

from collections import Counter
count = Counter(str1)
print(count)
    
    
        
    
    