x , y = map(int, input("Enter Your two nunber :").split(','))
print(x,y)

arr = [[i * j for j in range(y)] for i in range(x)]

print(arr)

# str1 = ["without","hello","bag","world"]

# words=[x for x in str1.split(',')]
# print(words)
# words.sort()

# print(sorted(str1))

# def sort_words(str1):
#     text =[x for x in str1.split(',')]
#     text.sort()
#     return text

# print(sort_words(str1))    