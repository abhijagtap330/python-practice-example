def count_of_string(string):
    count = 0
    for i in string:
        if len(i) > 2 and i[0] == i[-1]:
           count += 1
    return count

list1 = ["abba", "abc", "a", "racecar", "hello", "noon", "xyx"] 

print(count_of_string(list1)) 