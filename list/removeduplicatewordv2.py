lst = ["a", "b", "a", "b", "c", "d"]

i = 0
while i < len(lst):
    if lst[i] in lst[:i]:
        lst.pop(i)  # Remove the duplicate item
    else:
        i += 1  # Only increment if the item is unique

print(lst)

while i < len(lst):
    if lst[i] in lst[:i]:
        del [i]
    else:
        i += 1
        
        
lst = ["a", "b", "a", "b", "c", "d"]

print(lst)
for i, index in enumerate(lst):
    # print(index)
    for j in index:
        print(j)
        print(index[j].count < 2 )