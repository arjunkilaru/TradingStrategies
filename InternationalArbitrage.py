class InternationalArbitrageTrader:
    def __init__(self, asset, exchanges):
        self.asset = asset
        self.exchanges = exchanges

    def trade(self):
        # Initialize the best bid and ask prices and exchanges
        best_bid_price = 0
        best_bid_exchange = None
        best_ask_price = float("inf")
        best_ask_exchange = None

        # Iterate over the exchanges
        for exchange in self.exchanges:
            # Get the current bid and ask prices for the asset on this exchange
            bid_price, ask_price = exchange.get_bid_ask(self.asset)

            # Update the best bid and ask prices and exchanges if necessary
            if bid_price > best_bid_price:
                best_bid_price = bid_price
                best_bid_exchange = exchange
            if ask_price < best_ask_price:
                best_ask_price = ask_price
                best_ask_exchange = exchange

        # If the best bid price is higher than the best ask price,
        # there is an arbitrage opportunity
        if best_bid_price > best_ask_price:
            # Buy the asset on the exchange with the best ask price
            best_ask_exchange.buy(self.asset, 1, best_ask_price)
            # Sell the asset on the exchange with the best bid price
            best_bid_exchange.sell(self.asset, 1, best_bid_price)
            # Return the profit from the trade
            return best_bid_price - best_ask_price
        # If there is no arbitrage opportunity, return 0
        else:
            return 0
          
# Initialize the international arbitrage trader with the asset and a list of exchanges
international_arbitrage_trader = InternationalArbitrageTrader("AAPL", [exchange1, exchange2, exchange3])

# Check for arbitrage opportunities and execute trades if necessary
profit = international_arbitrage_trader.trade()

# Output: 0.1
print(profit)
