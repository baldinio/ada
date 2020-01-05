import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as hiclu
import scipy.spatial.distance as spad
import utils.functions as funs
import utils.graphics as plots


in_file = 'data/Teritorial2016/Indicatori.csv'
t = pd.read_csv(in_file, index_col=0)
funs.replace_na_df(t)
vars = list(t)
print(vars)

x = t[vars[3:]].values
# print(x)

# Observation classification
method_obs = list(hiclu._LINKAGE_METHODS)
print(method_obs)
metric_obs = spad._METRICS_NAMES
print(metric_obs)
h = hiclu.linkage(x, method=method_obs[5], metric=metric_obs[7])
print(h)

# Build partition tables
partitions = pd.DataFrame(index=t.index)
print("Partitions: \n", partitions)

# Determine the optimal partition
m = np.shape(h)[0]
print("m = ", m)
j = np.argmax(h[1:m, 2] - h[:(m - 1), 2])
print("j = ", j)
k = m - j
print("k = ", k)
g_optimal = funs.partition(h, k)
print("optimal partition = ", g_optimal)
partitions['Optimal_Partition'] = g_optimal

threshold = (h[j, 2] + h[j + 1, 2]) / 2
print("threshold value = ", threshold)

plots.dendrogram(h, t.index, "Observation Classifications | Method:" + method_obs[5] + " | Metric:" + metric_obs[7],
                    threshold=threshold)
plots.show()

# Partition with 7 groups
k = 7
g = funs.partition(h, k)
partitions['Partition_' + str(k)] = g
threshold = (h[m-k, 2] + h[m-k + 1, 2]) / 2
plots.dendrogram(h, t.index, "Partition with " + str(k) + " groups", threshold=threshold)
plots.show()
partitions.to_csv("partitions.csv")

# Variable classification
method_var = list(hiclu._LINKAGE_METHODS)
print(method_var)
metric_var = spad._METRICS_NAMES
print(metric_var)
h_v = hiclu.linkage(x.transpose(), method=method_var[2], metric=metric_var[4])
plots.dendrogram(h_v, vars, "Variable Classifications | Method:" + method_var[2] + " | Metric:" + metric_var[4])
plots.show()
