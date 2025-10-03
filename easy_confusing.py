import copy

x = 5
y = copy.copy(x)
x = 10
print(y)


def my_func(x, y=[]):
    y.append(x)
    return y

print(my_func(1))
print(my_func(2, []))
print(my_func(3))

x = 10
y = 10
z = 10
print(x is y is not z)

x = "Hello"
y = "hello"
print(x is not y)

a = [1, 2, 3]
b = a
b[0] = 100
print(a)


x = [1, 2, 3, 4]
y = x
y = y * 2
print(x)
print(y)

x = {1, 2, 3}
y = {3, 2, 1}
print(x == y)

a = [1, 2, 3]
b = a[:]
b[0] = 100
print(a)
print(b)

s = "abhijeet jagtap"
reversed_s = ""

# Loop through the string in reverse order and build the reversed string
for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]

print(reversed_s)

    
    