arr = list(map(int,input().split()))
b = int(input())
s = len(arr)
for i in range(s):
    for j in range(i+1,s):
        if arr[i]+arr[j]==b:
            print(1)
        else:
            print(0)
