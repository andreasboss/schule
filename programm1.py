import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)  # Start, Stop, Step
y = np.sin(x)

plt.plot(x, y, 'bo')
plt.axis( [0, 7, -1.5, 1.5] )
plt.grid(True)
plt.show()


