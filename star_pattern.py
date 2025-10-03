# Number of rows in the pattern
n = 10

# Loop to print the first half of the pattern
for i in range(1, n+1):
    print('*' * i)

# Loop to print the second half of the pattern
for i in range(n-1, 0, -1):
    print('*' * i)
    
for i in range(1,n+1):
    print(' ' * (n-i),end='')
    print('* ' * i)
    
import math

n = 2
sum_series = 0
for i in range(n,n+1):
    term = i / math.factorial(i)
    sum_series += term

print(sum_series)