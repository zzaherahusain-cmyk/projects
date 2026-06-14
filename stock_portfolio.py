class Stock:
    def __init__(self, name, qty, buy_price):
        self.name = name
        self.qty = qty
        self.buy_price = buy_price

    def investment(self):
        return self.qty * self.buy_price


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, name, qty, buy_price):
        stock = Stock(name, qty, buy_price)
        self.stocks.append(stock)

    def show_profit_loss(self, current_prices):
        total_investment = 0
        total_current = 0

        print("\n--- Portfolio Report ---")

        for stock in self.stocks:
            current_price = current_prices.get(stock.name, 0)

            invest = stock.investment()
            current_value = stock.qty * current_price

            profit_loss = current_value - invest

            total_investment += invest
            total_current += current_value

            print(f"{stock.name}: Invested = {invest}, Current = {current_value}, P/L = {profit_loss}")

        print("\nTOTAL INVESTMENT:", total_investment)
        print("TOTAL CURRENT VALUE:", total_current)
        print("TOTAL PROFIT/LOSS:", total_current - total_investment)


# ---------------- MAIN ----------------
p = Portfolio()

p.add_stock("TCS", 5, 3000)
p.add_stock("INFY", 10, 1500)
p.add_stock("RELIANCE", 2, 2500)

current_prices = {
    "TCS": 3200,
    "INFY": 1400,
    "RELIANCE": 2800
}

p.show_profit_loss(current_prices)