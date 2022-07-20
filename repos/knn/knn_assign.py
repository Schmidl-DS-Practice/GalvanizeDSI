from src.make_data import make_data

X, y = make_data(n_features=2, n_pts=300, noise=0.1)

print(X, y)