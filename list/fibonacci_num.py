n1=0
n2=1

for i in range(2,10):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
    
from itertools import combinations
numbers = [1,2,3,4]

for i in range(1,len(numbers) + 1):
    for combo in combinations(numbers,i):
        print(combo)

# from pandas.core.common import flatten # type: ignore


# test_list = [[1,3,"gfg"], [4,5], [6,"best"]]
 
# print(set(flatten(test_list)))

n1 = 0
n2 = 1
for i in range(1,3):
    sum = n1+n2
    n1 = n2
    n2 = sum
print(sum)
    