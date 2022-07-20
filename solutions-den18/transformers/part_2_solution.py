class OneHotEncoder:
    """A transformer for one-hot encoding a categorical feature.
    
    Attributes:
    levels: np.array
      The unique levels in the feature.  Computed when `fit` is called.
    """
    def __init__(self):
        self.levels = None
        self.name = None

    def fit(self, X, *args, **kwargs):
        self.levels = np.unique(X)
        if isinstance(X, pd.Series):
            self.name = X.name
        return self

    def transform(self, X, **transform_params):
        output = np.zeros((len(X), len(self.levels)))
        for i, level in enumerate(self.levels):
            output[:, i] = (X == level).astype(int)
        if isinstance(X, pd.Series):
            output = pd.DataFrame(output)
            output.columns = self._compute_column_names()
        return output
    
    def _compute_column_names(self):
        return np.array([self.name + "_is_" + level for level in self.levels])
