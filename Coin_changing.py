coins = list(map(int, input().split()))
coins.sort(reverse = True)

amount= int(input())

change = []
for coin in coins:
      
    if coin <= amount:
        change.append(coin)
        amount -= coin
        
    else:
        break

print(change)

