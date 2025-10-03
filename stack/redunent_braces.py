def redunant_braces(N):
    
    stack = []
    
    for i in range(len(N)):
        if (N[i] in "(+-*/"):
             stack.append(N[i])
             
        elif(N[i] == ")"):
            if stack.pop() == "(":
                return 1
            
            stack.pop()
    return 0

N = "((a+b) * 6)"
a = redunant_braces(N)

if a == 1:
    print("Redandant")
else:
    print("Not Redundant") 