def flatten_list(nested_list):
    extened = []
    for i in nested_list:
        if isinstance(i, list):
            extened.extend(i)
        else:
            extened.append(i)
            
    return extened

lst = [12,2,[2,3],4,[5,7]]
print(flatten_list(lst))