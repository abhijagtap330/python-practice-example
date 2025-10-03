# factorial = 1
# num = 0
#
# if num < 0:
#     print("Factorial of 0 is 1")
# elif num==0:
#     print("Factorial does not extis for negative number")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("Factorial value of",num,"is",factorial)
#
#


def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    # return 1 if (n==0 or n==1) else n*factorial(n-1)
num = 10
print(factorial(num))


def factorial_num(num):
    if (num == 0 or num ==1):
        return 1
    else:
        return num * factorial(num -1)

num=5
print(factorial_num(num))