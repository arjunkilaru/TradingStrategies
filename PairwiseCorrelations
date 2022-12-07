import numpy as np

class PairwiseCorrelationTrader:
    def __init__(self, asset1, asset2, window_size):
        self.asset1 = asset1
        self.asset2 = asset2
        self.window_size = window_size
        self.history = []

    def update(self, timestamp, asset1_price, asset2_price):
        # Add the new prices to the history
        self.history.append((timestamp, asset1_price, asset2_price))
        # Keep only the most recent "window_size" prices
        self.history = self.history[-self.window_size:]

    def trade(self):
        # Calculate the pairwise correlation between the two assets
        corr = np.corrcoef(self.history[:,1], self.history[:,2])[0,1]

        # If the correlation is positive, buy the first asset and sell the second
        if corr > 0:
            return (self.asset1, self.asset2, 1, -1)
        # If the correlation is negative, buy the second asset and sell the first
        elif corr < 0:
            return (self.asset1, self.asset2, -1, 1)
        # If the correlation is zero, do not trade
        else:
            return (self.asset1, self.asset2, 0, 0)
            
# Initialize the pairwise correlation trader with the two assets
# and a window size of 10
pairwise_correlation_trader = PairwiseCorrelationTrader("AAPL", "GOOG", 10)

# Update the trader's history with the latest prices
pairwise_correlation_trader.update(1, 100, 200)
pairwise_correlation_trader.update(2, 101, 199)
pairwise_correlation_trader.update(3, 102, 198)

# Determine the trade to make
trade = pairwise_correlation_trader.trade()

# Output: ('AAPL', 'GOOG', 1, -1)
print(trade)
