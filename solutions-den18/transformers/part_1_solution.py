class OneHotEncoder:
    """A transformer for one-hot encoding a categorical feature.
    
    Attributes:
    levels: np.array
      The unique levels in the feature.  Computed when `fit` is called.
    """
    def __init__(self):
        self.levels = None

    def fit(self, X, *args, **kwargs):
        self.levels = np.unique(X)
        return self

    def transform(self, X, **transform_params):
        output = np.zeros((len(X), len(self.levels)))
        for i, level in enumerate(self.levels):
            output[:, i] = (X == level).astype(int)
        return output
