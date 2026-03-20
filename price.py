import random
import time

def max_profit_robust(prices):
    if len(prices) < 2:
        return None
    min_price = prices[0]
    max_profit = float('-inf')
    for price in prices[1:]:
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)
        min_price = min(min_price, price)
    return max_profit

T1 = [2, 7, 5, 8, 11, 9]
T4 = [6, 5, 4, 3, 2, 1]
T3 = [1,1,1,1,1,1,1]

print(max_profit_robust(T1))
print(max_profit_robust(T4))
print(max_profit_robust(T3))

#add simulation check

large_prices = [random.randint(1, 100) for i in range(10000000)]

start_time = time.time()
result = max_profit_robust(large_prices)
end_time = time.time()

print(result)
print(end_time-start_time)