import random

def get_stock_prediction(stock_data):
    if len(stock_data) == 0:
        return "No data available"
    return random.choice(["Buy", "Sell", "Hold"])