def knapsack(n,capacity,weights,prices):
    if(n==0 or capacity==0):
        return 0
   
    else:
        return max(prices[n-1] + knapsack(n-1,capacity-weights[n-1],weights,prices),
                   knapsack(n-1,capacity,weights,prices))
 
weights = list(map(int, str(input()).split()))
prices = list(map(int, str(input()).split()))
n = len(weights)
capacity = int(input())
 
print(knapsack(n,capacity,weights,prices))
















 
