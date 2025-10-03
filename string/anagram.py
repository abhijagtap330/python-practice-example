str1 = "Abhi"
str2 = "ihbA"

def anagram(str1,str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False

if anagram(str1,str2):
    print("Anagram")
else:
    print("Not Anagram")