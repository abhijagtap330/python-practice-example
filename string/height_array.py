values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))



s = input("Enter your numbers:")
# print(s.split(','))

# items=[x for x in input().split(',')]
# print(items)
a = [i for i in s.split(',') if int(i)%2 != 0]
print(a)