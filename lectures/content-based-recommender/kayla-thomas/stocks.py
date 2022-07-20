#!/usr/bin/env python
# adapted from file from https://github.com/nicodv/kmodes/tree/master/examples

import numpy as np
from kmodes.kprototypes import KPrototypes

# stocks with their market caps, sectors and countries
syms = np.genfromtxt('stocks.csv', dtype=str, delimiter=',')[:, 0]
X = np.genfromtxt('stocks.csv', dtype=object, delimiter=',')[:, 1:]
X[:, 0] = X[:, 0].astype(float)


print("\nData:")
print("symbol\tprice\ttype\tregion")
for sym, row in zip(syms, X):
    price, typ, region = row
    print("{0}\t{1}\t{2}\t{3}".format(sym, price, typ.decode('utf-8'), region.decode('utf-8')))

print('\nClustering:')
k = 4
kproto = KPrototypes(n_clusters=k, init='Cao', verbose=2)
clusters = kproto.fit_predict(X, categorical=[1, 2])

# Print cluster centroids of the trained model.
print(kproto.cluster_centroids_)
# Print training statistics
print(kproto.cost_)
print(kproto.n_iter_)

print("\nUsing {} clusters:".format(k))
for s, c in zip(syms, clusters):
    print("Symbol: {}, cluster:{}".format(s, c))
