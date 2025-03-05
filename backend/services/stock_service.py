def fetch_stock_data(symbol):
    sample_data = {
        "AAPL": [150, 152, 149, 153],
        "GOOGL": [2800, 2820, 2790, 2815]
    }
    return sample_data.get(symbol.upper(), [])