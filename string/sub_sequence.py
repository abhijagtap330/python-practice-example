def subsequence(string):
  
  if len(string) == 0:
    return [" "]
  
  small = subsequence(string[1:len(string)])
  result = [" "]* (2*len(small))
  k = 0
  
  for i in range(len(small)):
    result[k] = small[i]
    k = k+1
    
  for i in range(len(small)):
    result[k] = string[0] + small[i]
    k = k+1
    
  return result 
  
print(subsequence("Net"))