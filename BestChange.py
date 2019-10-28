import math


#This function takes a float as a parameter, and prints out two arrays, which contain
#how the parameter can be represented using the least amount of currency
def best_change(change):
    paper_money = [100, 50, 20, 5, 1]
    coins = [25, 10, 5, 1]
    paper_money_change = []
    coin_array = []

    paper_change = math.floor(change)
    coin_change = math.floor(round(change - paper_change, 2)*100)

    for dollar in paper_money:
        for bills in range(paper_change//dollar):
            paper_money_change.append(dollar)
            paper_change -= dollar
        if paper_change == 0:
            break

    for coin in coins:
        for a_coin in range(coin_change//coin):
            coin_array.append(coin)
            coin_change -= coin
        if coin_change == 0:
            break

    print("Bills: %a" % paper_money_change)
    print("Coins: %a" % coin_array)


cost = float(input("Total Cost: "))
paid = float(input("Amount Received: "))
print("\nChange: ")
best_change(paid-cost)











