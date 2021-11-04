def partition(arr, start, end):
    i = (start-1) 
    pivot = arr[end]
  
    for j in range(start, end):
  
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return (i+1)
   
def quickSort(arr, start, end):
    if len(arr) == 1:
        return arr
    if start < end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)
  
arr = list(map(int, input().split()))
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
    
    
    
    