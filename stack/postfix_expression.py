def eval_expression(array):
    
    stack = []
    operator = ["+", "-", "*", "/", "%"]
    
    for item in array:
        if item not in operator:
            stack.append((item))
        else:
            first = int(stack.pop())
            second = int(stack.pop())
            
        if(item=="+"):
            stack.append(second + first)
        
        if(item=="-"):
            stack.append(second - first)
            
        if(item=="*"):
            stack.append(second * first)
            
        if(item=="/"):
            stack.append(second / first)
            
        if(item=="%"):
            stack.append(second % first)
    
    return stack[-1]
        
print(eval_expression(["2", "1", "+", "3", "*"]))