import pandas as pd
import numpy as np

# Creare pandas DataFrame din Python dictionary
d1 = {"col1":[1, 2, 3], "col2":[4, 5, 6], "col3":[7, 8, 9]}
print(d1)
df0 = pd.DataFrame(d1)
print(df0)
print(df0.index)
print(df0.columns)
print(df0.values)

# Scriere pandas DataFrame in fisier .csv
df0.to_csv('df_din_dictionar.csv')

# Citire fisier .csv in pandas DataFrame
tabel = pd.read_csv('df_din_dictionar.csv', index_col=0)
print(tabel)

# Functie pentru generat <size> numere aleatoare in intervalul [low, high]
def Random(low=None, high=None, size=None):
    return ((high - low) * np.random.rand(size) + low)

# Dictionary comprehension
d2 = {'col'+str(i):Random(-1, 1, 10) for i in range(1, 5+1)}
df1 = pd.DataFrame(d2, index=('lin'+str(i) for i in range(1, 10+1)))
print(df1)

# List comprehension pentru generarea unei colectii de numere aleatoare intr-un interval de valori dat
l2 = Random(11, 12, 25)
print(l2)
print(l2.shape)
print(l2.itemsize)

# Creare numpy ndarray dintr-o lista de valori de tip <float>
npa = np.ndarray(shape=(5, 3), dtype=float, buffer=l2, order='C')
print("Numpy ndarray: \n", npa)

# Creare numpy ndarray dintr-o lista cu un anumit offset
print('Dimensiune element lista: ', l2.itemsize)
npa1 = np.ndarray(shape=(5, 4), dtype=float, buffer=l2, offset=l2.itemsize*5)
print(npa1)
print(npa1.shape)
df2 = pd.DataFrame(npa1)
print(df2)

df3 = pd.DataFrame(npa1)
print(df3)
df3.to_csv('pd_df.csv')

#Creare pandas DataFrame din numpy ndarray
df2 = pd.DataFrame(npa1, index=('L'+str(i+1) for i in range(npa1.shape[0])),
                   columns=('C'+str(j+1) for j in range(npa1.shape[1]))) # we provide d tuples for index and columns
print(df2)

# Scriere pandas DataFrame in fisier .csv
df2.to_csv('exemplu_df.csv')

