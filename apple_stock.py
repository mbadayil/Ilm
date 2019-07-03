stock_prices = [10, 7, 5, 8, 11, 9]
def stockPrice(stock_prices):
    if len(stock_prices)<2:
        return False
    return max(stock_prices)-min(stock_prices)

stockPrice(stock_prices)
