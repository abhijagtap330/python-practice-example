def palindrome_number(number):
    
    string = str(number)
    
    if string == string[::-1]:
        print("This is palindrome Number")
    else:
        print("This is not palindrome number")
        
number = 123221

palindrome_number(number)


# Take input from the user
input_string = input("Enter a string: ")

# Initialize an empty string to store the result
title_case_string = ""

# Split the input string into words
words = input_string.split()
print(words)
# Process each word
for word in words:
    # Capitalize the first letter and keep the rest in lowercase
    if len(word) > 0:  # Check if the word is not empty
        title_case_word = word[0].upper() + word[1:].lower()
        title_case_string += title_case_word + " "

# Remove the trailing space and print the result
title_case_string = title_case_string.strip()
print(f"The title case string is: '{title_case_string}'")
