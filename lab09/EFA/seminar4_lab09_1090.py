import numpy as np
import matplotlib.pyplot as plt

x = [np.cos(t) for t in np.arange(0, np.pi * 2, 0.01)]
print(x)
y = [np.sin(t) for t in np.arange(0, np.pi * 2, 0.01)]
print(y)

plt.plot(x, y)
plt.axhline(0, 0, color="green")
plt.axvline(0, 0, color="green")
plt.show()
