arr = list(map(int,input("Enter a list").split()))
count = 0
s = max(arr)
for i in range(arr):
    if s>i:
        count+=1
print(count)
