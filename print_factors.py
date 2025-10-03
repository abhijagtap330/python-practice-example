factor = []
def print_factor(n):
    for i in range(1,n+1):
        if n % i == 0:
            factor.append(i)
    return factor


print(print_factor(1203467))