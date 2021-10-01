lst = list(map(int, input(). split()))
lst.sort()

key = int(input())
start = 0
end = len(lst)-1

while start <= end:
    mid = start+end//2
    if lst[mid] < key:       
        start = mid + 1
    elif lst[mid] > key:
         end = mid - 1
    else:
         return mid
return -1


        

    

    
 
    
    
    
    