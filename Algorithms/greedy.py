def min_coins_greedy(coins, amount):
    coins.sort(reverse=True)  # Büyükten küçüğe sırala
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count

coins = [1, 5, 10]
amount = 18
print(min_coins_greedy(coins, amount))  # Çıktı: 5 (1x10 TL, 1x5 TL, 3x1 TL)
