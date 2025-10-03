arr=[1,2,3,4,5,10]

max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print(max)