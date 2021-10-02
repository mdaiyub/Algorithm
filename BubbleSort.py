def bubblesort(array):
    n = len(array)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            if array[j] > array[j+1]:
                array[j], array[J+1] = array[J+1], array[j]
                
array = [12,23,34,56,67,89,123,234,345]   
bubblesort(array)  

print("Bubble Sorted array is:\n ")
for i in range (len(array)):
    print(array[i])
    
           
            