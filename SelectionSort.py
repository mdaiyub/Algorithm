def selection(mylist):
   
    for i in range(len(your_data)):
        min_idx = i

        for j in range(i + 1, len(your_data)):
            if mylist[j] < mylist[min_idx]:
                min_idx = j
        mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]


your_data = list(map(int, input().split()))
selection(your_data)
print(your_data)

print("Time Complexity=n^2")




