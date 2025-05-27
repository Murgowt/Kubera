import yfinance as yf

def fetch_prices_core(symbol):
    try:
        stock = yf.Ticker(f"{symbol}.NS")
        return stock.info["regularMarketPrice"]
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None


def fetch_prices(stock_list):
    results = []
    for row in stock_list:
        _, symbol, name, _, _ = row
        price = fetch_prices_core(symbol)
        if price is not None:
            results.append({
                'name': name,
                'symbol': symbol,
                'price': price
            })
    return results