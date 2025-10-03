def string_compressed(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count)) #converting into the string
            count = 1
    compressed.append(s[-1] + str(count)) #for last element 
        
    compressed_str = "".join(compressed)
    return compressed_str
        
print(string_compressed("aabcccccaaa"))