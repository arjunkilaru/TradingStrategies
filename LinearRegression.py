import numpy as np

class LinearRegressionTrader:
    def __init__(self, asset, window_size):
        self.asset = asset
        self.window_size = window_size
        self.history = []

    def update(self, timestamp, price):
        # You can link this to a server that can continually update the trader class with prices
        # Add the new price to the history
        self.history.append((timestamp, price))
        # Keep only the most recent "window_size" prices
        self.history = self.history[-self.window_size:]

    def trade(self):
        # Fit a linear regression model to the historical data
        x = [h[0] for h in self.history]
        y = [h[1] for h in self.history]
        (a, b) = np.polyfit(x, y, 1)

        # Use the linear regression model to make a prediction
        # about the future price of the asset
        future_timestamp = max(x) + 1
        future_price = a * future_timestamp + b

        # If the predicted future price is higher than the current price,
        # take a long position in the asset
        if future_price > self.history[-1][1]:
            return (self.asset, 1)
        # If the predicted future price is lower than the current price,
        # take a short position in the asset
        elif future_price < self.history[-1][1]:
            return (self.asset, -1)
        # If the predicted future price is the same as the current price,
        # do not trade
        else:
            return None


# Initialize the linear regression trader with the asset
# and a window size of 10
linear_regression_trader = LinearRegressionTrader("AAPL", 10)

# Update the trader's history with the latest prices
linear_regression_trader.update(1, 100)
linear_regression_trader.update(2, 101)
linear_regression_trader.update(3, 102)

# Determine the trade to make
trade = linear_regression_trader.trade()

# Output: ('AAPL', 1)
print(trade)
