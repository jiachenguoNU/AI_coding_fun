import numpy as np
import matplotlib.pyplot as plt


sigmoid_y = [1./(1+ np.exp(-x)) for x in [-200, -1, -0.9, -0.3, 0, 0.3, 0.9, 1] if x>= -1]
x = [-1, -0.5, -0.3, 0, 0.3, 0.5, 1]
plt.figure()
plt.plot(x, sigmoid_y)
plt.savefig('sigmoid')
