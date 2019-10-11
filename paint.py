import numpy as np
from matplotlib import pyplot as plt

prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
x = np.arange(1, len(prices) + 1)
y = prices
plt.title('Stock prices')
plt.xlabel('Days')
plt.ylabel('Prices')
plt.plot(x, y)
plt.show()
