import numpy as np
import pandas as pd
import matplotlib.pyplot as plt     #import biblioteca grafica matplotlib
import seaborn as sb                #import biblioteca grafica seaborn


#citire date din fisier csv
tabel = pd.read_csv("teritorial.csv",index_col=0)

#Extragere valori prelucrate in matrice ndarray (numpy)
X = tabel.iloc[:,2:].values
#print(X)

nume_instante = tabel.index
nume_coloane = tabel.columns[2:]
n = X.shape[0]
m = X.shape[1]
print(m, n)
print(nume_coloane)
print(nume_instante)

#Salvare tabel prelucrat
X_Tab = pd.DataFrame(data=X,columns=nume_coloane,index=nume_instante)
print(X_Tab)
X_Tab.to_csv(path_or_buf="X.csv")

#Calcul matrice de corelatie
R = np.corrcoef(X,rowvar=False)
R_Tab = pd.DataFrame(data=R,columns=nume_coloane,index=nume_coloane)
R_Tab.to_csv(path_or_buf="R.csv")

#Afisare corelograma
plt.figure("Corelograma",figsize=(8,7))
sb.heatmap(data=R_Tab,vmin=-1,vmax=1,cmap='bwr')
plt.title("Corelgrama corelatii tabel")
plt.show()
