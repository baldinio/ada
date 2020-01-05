import numpy as np
import matplotlib.pyplot as mpl

x = [np.cos(t) for t in np.arange(0, np.pi * 2, 0.01)]
print("x=", x)
y = [np.sin(t) for t in np.arange(0, np.pi * 2, 0.01)]
print("y=", y)

mpl.plot(x, y)
mpl.axhline(0, color="g")
mpl.axvline(0, color="g")
mpl.xlabel("first PC")
mpl.ylabel("second PC")
mpl.show()


def normalize(X):
    XMin = np.min(X, axis=0)
    # print(xMin)
    XMax = np.max(X, axis=0)
    XNorm = (X - XMin) / (XMax - XMin)
    return XNorm


def standardize(X):
    means = np.mean(X, axis=0)
    stdv = np.std(X, axis=0);
    return (X - means) / stdv
