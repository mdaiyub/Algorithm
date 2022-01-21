arr = list(map(int, input().split()))
key = int(input())

flag = 0

for i in range(len(arr)): 
        if (arr[i] == key):
            flag = 1
            position = i
            break
        
if flag == 1:
    print("Item found at index:", position)
    
else:
    print("Item not Found.")

    