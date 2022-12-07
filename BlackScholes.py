def black_scholes(S, K, T, r, sigma, option):
    # Calculate the d1 and d2 terms
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Calculate the Black-Scholes price
    if option == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        return price
    if option == 'put':
        price = K*np.exp(-r * T)*(norm.cdf(-1*d2)) - S* norm.cdf(-1*d1)
        return price
      
def black_scholes_greeks(S, K, T, r, sigma):
    # Calculate the d1 and d2 terms
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Calculate the option's value
    value = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

    # Calculate the option's delta
    delta = norm.cdf(d1)

    # Calculate the option's gamma
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))

    # Calculate the option's theta
    theta = -(S * sigma * norm.pdf(d1)) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)

    # Return the option's value, delta, gamma, and theta
    return (value, delta, gamma, theta)
