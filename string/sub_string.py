def substring(str1,n):
    
    for i in range(n):
        for j in range(i+1,n+1):
            print(string[i:j])


string = 'Abhijeet'        
n=len(string)
print(substring(string,n))