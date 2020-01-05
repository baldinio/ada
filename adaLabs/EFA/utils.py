import numpy as np
import pandas as pd
import scipy.stats as sts
import pandas.api.types as pdt


# Replace NA (not available, not applicable) or NaN (not a number) cells
# with column (variable) mean
# for a pandas DataFrame
def replace_NA(X):
    avgs = np.nanmean(X, axis=0)
    pos = np.where(np.isnan(X))
    print(pos[:])
    X[pos] = avgs[pos[1]]
    return X

# Standardize the column (variable) values
# for a pandas DataFrame
def standize(X):
    avgs = np.mean(X, axis = 0 )
    stds = np.std(X, axis = 0)
    Xstd = (X - avgs) / stds
    return Xstd

def standardizare(X):
    medii = np.mean(X, axis=0)
    abaterestd = np.std(X, axis=0)
    Xstd = (X - medii) / abaterestd
    return Xstd


def inversare(t, y=None):
    if type(t) is pd.DataFrame:
        for c in t.columns:
            minim = t[c].min();
            maxim = t[c].max()
            if abs(minim) > abs(maxim):
                t[c] = -t[c]
                if y is not None:
                    k = t.columns.get_loc(c)
                    y[:, k] = -y[:, k]
    else:
        for i in range(np.shape(t)[1]):
            minim = np.min(t[:, i]);
            maxim = np.max(t[:, i])
            if np.abs(minim) > np.abs(maxim):
                t[:, i] = -t[:, i]


def acp(X):
    R = np.corrcoef(X, rowvar=False)
    # calcul vector si valori proprii
    valp, vecp = np.linalg.eig(R)
    # sortare valori proprii si vectori proprii
    k_inv = [k for k in reversed(np.argsort(valp))]
    alpha = valp[k_inv]
    a = vecp[:, k_inv]
    inversare(a)
    # calcul corelatii factoriale
    Rxc = a * np.sqrt(alpha)
    # calcul componente
    # standardizare X
    medii = np.mean(X, axis=0)
    abaterestd = np.std(X, axis=0)
    Xstd = (X - medii) / abaterestd
    C = Xstd @ a
    return R, alpha, a, Rxc, C

# Functie pentru inlocuirea valorilor lipsa
# prin medie/modul
def inlocuire_na_df(t):
    for c in t.columns:
        if pdt.is_numeric_dtype(t[c]):
            if t[c].isna().any():
                medie = t[c].mean()
                t[c] = t[c].fillna(medie)
        else:
            if t[c].isna().any():
                modul = t[c].mode()
                t[c] = t[c].fillna(modul[0])


def inlocuire_na(X):
    medii = np.nanmean(X, axis=0)
    k_nan = np.where(np.isnan(X))
    X[k_nan] = medii[k_nan[1]]

def tabelare_varianta(alpha):
    m = len(alpha)
    varianta_cumulata = np.cumsum(alpha)
    procent_varianta = alpha * 100 / m
    procent_cumulat = np.cumsum(procent_varianta)
    tabel_varianta = pd.DataFrame(data={"Varianta": alpha,
                                        "Varianta Cumulata": varianta_cumulata,
                                        "Procent varianta": procent_varianta,
                                        "Procent cumulat": procent_cumulat
                                        })
    tabel_varianta.to_csv("varianta.csv")

def tabelare(X, nume_coloane=None, nume_instante=None, tabel=None):
    X_tab = pd.DataFrame(X)
    if nume_coloane is not None:
        X_tab.columns = nume_coloane
    if nume_instante is not None:
        X_tab.index = nume_instante
    if tabel is None:
        X_tab.to_csv("tabel.csv")
    else:
        X_tab.to_csv(tabel)
    return X_tab

def evaluate(C, alpha, R):
    n = np.shape(C)[0]
    # Compute scores
    S = C / np.sqrt(alpha)
    # Compute cosines
    C2 = C * C
    suml = np.sum(C2, axis=1)
    q = np.transpose(np.transpose(C2) / suml)
    # Compute contributions
    beta = C2 / (alpha * n)
    # Compute commonalities
    R2 = R * R
    Comun = np.cumsum(R2, axis=1)
    return S, q, beta, Comun

def bartlett_test(n, l, x, e):
    m, q = np.shape(l)
    v = np.corrcoef(x, rowvar=False)
    psi = np.diag(e)
    v_ = l @ np.transpose(l) + psi
    I_ = np.linalg.inv(v_) @ v
    det_v_ = np.linalg.det(I_)
    trace_I = np.trace(I_)
    chi2 = (n - 1 - (2 * m + 4 * q - 5) / 2) * (trace_I - np.log(det_v_) - m)
    g_lib = ((m - q) * (m - q) - m - q) / 2
    p_value = sts.chi2.cdf(chi2, g_lib)
    return chi2, p_value

def bartlett_factor(x):
    n, m = np.shape(x)
    r = np.corrcoef(x, rowvar=False)
    chi2 = -(n - 1 - (2 * m + 5) / 6) * np.log(np.linalg.det(r))
    g_lib = m * (m - 1) / 2
    p_value = 1 - sts.chi2.cdf(chi2, g_lib)
    return chi2, p_value

def bartlett_wilks_test(r, n, p, q, m):
    r_inv = np.flipud(r)
    l = np.flipud(np.cumprod(1-r_inv*r_inv))
    dof = (p-np.arange(m))*(q-np.arange(m))
    chi2 = (-n+1+(p+q+1)/2)*np.log(l)
    p_value = 1 - sts.chi2.cdf(chi2,dof)
    return p_value
