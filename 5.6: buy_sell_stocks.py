prices = [310,315,275,295,260,270,290,230,255,250]
max_profit = float("-inf")
buy = 0
sell = 0
for i in range(len(prices)):
    
    for j in range(i,len(prices)):
        if max_profit < (prices[j] - prices[i]):
            max_profit = prices[j] - prices[i]
            buy = i
            sell = j

print("buy at:",prices[buy]," sell at:",prices[sell], " max_profit profit =",max_profit)

def buy_and_se11_stock_once (prices) :
    min_price_so_far , max_profit = float ('inf') , 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit
max_profit = buy_and_se11_stock_once(prices)
print(max_profit)