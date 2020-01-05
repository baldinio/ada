import graphics
import pandas as pd
import pca.PCA as pc

# Read input data from csv file
table = pd.read_csv("Teritorial.csv", index_col=0)

# Bring the table data into a numpy matrix (ndarray)
X = table.iloc[:, 1:].values

obs_name = table.index
var_name = table.columns[1:]

n = X.shape[0] # number of observation
m = X.shape[1] # number of variables
print(n, m)
print(X)

# Instantiate a PCA object
pca = pc.PCA(X)
R = pca.getCorrelation()
alpha = pca.getEigenValues()
a = pca.getEigenVectors()
Rxc = pca.getCorrelationFactors()
C = pca.getPrincipalComponents()
print(R)
print("Eigenvalues: ", alpha)
print("Eigenvectors: ", a)

# Save the processed table
X_Tab = pd.DataFrame(data=X, columns=var_name, index=obs_name)
X_Tab.to_csv(path_or_buf="X.csv")

# Save the correlation matrix
R_Tab = pd.DataFrame(data=R, columns=var_name, index=var_name)
R_Tab.to_csv(path_or_buf="R.csv")

# Show the correlogram
graphics.correlogram(R_Tab)

# Save the correlation factors
Rxc_Tab = pd.DataFrame(Rxc, index=var_name, columns=
                       ["C"+str(k+1) for k in range(m)])
Rxc_Tab.to_csv("Rxc.csv")
# print(R_Tab)

# Show factors correlogram
graphics.correlogram(Rxc_Tab, "Correlogram of the factors")
graphics.corrCircles(Rxc_Tab, 0, 1)

# Show the eigenvalues graphic
graphics.eighenValues(alpha)
