import yfinance as yf
import pandas as pd

# Portfolio example
portfolio = [
    {"ticker": "AAPL", "quantity": 10, "purchase_price": 145.00},
    {"ticker": "MSFT", "quantity": 5, "purchase_price": 250.00}
]

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return price

def calculate_portfolio(portfolio):
    total_value = 0
    details = []

    for stock in portfolio:
        current_price = fetch_stock_data(stock['ticker'])
        current_value = stock['quantity'] * current_price
        gain_loss = current_value - (stock['quantity'] * stock['purchase_price'])
        gain_loss_percent = (gain_loss / (stock['quantity'] * stock['purchase_price'])) * 100

        details.append({
            "ticker": stock['ticker'],
            "current_price": current_price,
            "current_value": current_value,
            "gain_loss": gain_loss,
            "gain_loss_percent": gain_loss_percent
        })

        total_value += current_value

    return total_value, details

# Display portfolio
total_value, details = calculate_portfolio(portfolio)
print(f"Total Portfolio Value: ${total_value:.2f}\n")
print("Stock Details:")
for stock in details:
    print(f"{stock['ticker']}: Current Price: ${stock['current_price']:.2f}, "
          f"Current Value: ${stock['current_value']:.2f}, "
          f"Gain/Loss: ${stock['gain_loss']:.2f} ({stock['gain_loss_percent']:.2f}%)")
