import numpy as np
import matplotlib.pyplot as plt

# f1 = open("graphics.py")
# linii = []
# for linie in f1:
#     print(linie[:-1])
#     linii.append(linie[:-1])
#
# print(linii)
# f1.close()

# with open('Teritorial.csv') as f2:
#     linii = []
#     for linie in f2:
#         cuvinte = linie[:-1].split(sep=',')
#         val = []
#         for v in cuvinte:
#             if v.isnumeric():
#                 val.append(float(v))
#             else:
#                 pass
#         linii.append(val)
#         print(val)
#
# num = linii[1:]
# print(num)

T = [t for t in np.arange(0, np.pi*2, 0.01)]
print(T)

X = [np.cos(t) for t in T]
Y = [np.sin(t) for t in T]

plt.figure("Cercul Corelatiilor", figsize=(7, 7))
plt.plot(X, Y)
plt.axvline(0, color='g')
plt.axhline(0, color='g')
plt.show()

