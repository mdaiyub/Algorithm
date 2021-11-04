My_list = list(map(int, input().split()))
   
list1 = []
list2 = []
for num in My_list :
    if num >= 0:
        list1.append(num)
    else:
        list2.append(num)
          
print("Positive numbers in the list: ", list1)
print("Negative numbers in the list: ", list2)


