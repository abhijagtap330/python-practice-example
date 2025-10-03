def remove_duplicate(num):
  nuique_number = []
  for i in num:
    if i not in nuique_number:
      nuique_number.append(i)
    #   sum_nuique = sum(nuique_number.append(i))
  return nuique_number

list1 = [1,1,12,13,12]
print(remove_duplicate(list1))


a1 = 0
a2 = 1

for i in range(2,10):
  sum = a1+a2
  print(sum)
  a1=a2
  a2=sum

