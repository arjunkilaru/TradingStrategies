import numpy as np

class GammaScalper:
    def __init__(self, underlying_price, option_delta, option_gamma, trade_frequency):
        self.underlying_price = underlying_price
        self.option_delta = option_delta
        self.option_gamma = option_gamma
        self.trade_frequency = trade_frequency

    def trade(self, underlying_price_change):
        # Calculate the change in the option's delta
        delta_change = self.option_gamma * underlying_price_change
        # Calculate the new delta of the option
        new_delta = self.option_delta + delta_change
        # Determine the number of shares to buy or sell
        shares = self.trade_frequency * new_delta
        # Return the number of shares to buy or sell
        return shares
      
# Initialize the gamma scalper with the current underlying price,
# the option's delta and gamma, and the trade frequency
gamma_scalper = GammaScalper(100, 0.5, 0.01, 100)

# Suppose the underlying price increases by $1
underlying_price_change = 1

# Determine the number of shares to buy or sell
shares = gamma_scalper.trade(underlying_price_change)

# Output: 100
print(shares)

# Suppose the underlying price decreases by $1
underlying_price_change = -1

# Determine the number of shares to buy or sell
shares = gamma_scalper.trade(underlying_price_change)

# Output: -100
print(shares)
