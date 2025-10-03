x = ["P", "Y", "T", "H", "O", "N"]
y = ["P", "Y", "T", "H", "O", "N"]

a = [1,2,3,4]
b = [1,2,3,4]

string = ''.join(x)
print(string)

final = [x+y for x, y in zip(x,y)]
print(final)
print(final)

c = a+b
print(c)