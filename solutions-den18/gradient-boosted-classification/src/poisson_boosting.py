import numpy as np
from sklearn.base import clone
from sklearn.tree import DecisionTreeRegressor


class GradientBoostingPoissonRegressor:
    """A Gradient Boosted Regression Tree model for conditionally Poisson
    distributed data.

    This model estimates a function f for which

        y | X ~ Poisson(lambda = exp(f(X)))

    The function f is estimated as a sum of regression trees by maximizing the
    log-likelihood of the Poisson model.

    Parameters
    ----------
    n_estimators: int
        A positive integer.  The number of regression trees to stack when
        estimating f.

    learning_rate: float
        A non-negative number which is less than one.  The amount of shrinkage
        to apply to an estimated regression tree before adding into f.

    max_depth: int
        Positive integer.  The maximum depth for the estimated regression trees.

    Attributes
    ----------
    n_estimators: int
        The number of regression trees to stack when estimating f.

    learning_rate: float
        The amount of shrinkage to apply to an estimated regression tree before
        adding into f.

    max_depth: int
        The maximum depth for the estimated regression trees.

    initial_value_: float
        The overall mean of y in the training data.  Used as an initial
        prediction, all subsequent regression trees predictions are added to
        this baseline value.

    estimators_: list of sklean.tree objects.
        Sequence of estimated regression trees.

    terminal_node_estimates_: list of dict(int: float)
        Predictions that apply in the terminal nodes (leaves) of the estimated
        regression trees.  These prediction are summed into the final
        predictions of the gradient boosted model.
    """
    def __init__(self, 
                 n_estimators=100,
                 learning_rate=0.001,
                 max_depth=2):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.weak_learner = DecisionTreeRegressor(max_depth=self.max_depth)
        # Estimated quantities.
        self.initial_value_ = None
        self.estimators_ = []
        self.terminal_node_estimates_ = []

    def fit(self, X, y):
        """Fit boosted model to training data.

        Gradient Boosting is fit in a forward stagewise manner.  In detail,
        this means that we start with a baseline working prediction, then
        continually fit a regression tree to the "residuals" of this working
        prediction, get predictions from the fit regression tree, and then use
        these predictions to update our overall working prediction.

        Parameters
        ----------
        X: array, shape (n_samples, n_features)
            Training data.

        y: array, shape (n_samples, )
            Target values.

        Returns
        -------
        self: GradientBoostingPoissonRegressor object
            The fit model.

        Notes
        -----
        This method uses the following internal data structures:

        working_prediction: array, shape (n_sample, )
            The current working prediction, equal to the baseline prediction
            plus the sum of the predictions of the currently fit sequence of
            regression trees.

        working_response: array, shape (n_samples, )
            The array of targets for the next regression tree.  Equal to the
            "residuals" of the current working_prediction.  The word
            "residuals" here should not be taken too literally (though in some
            cases it is true that the working response is the residuals), in
            general it is equal to the gradient of the loss function evaluated
            at the working prediction.

        Definitions of the other data structures used here are included in the
        corresponding methods that compute them.
        """
        self.initial_value_ = self._initial_value(y)
        working_prediction = np.repeat(self.initial_value_, y.shape[0])
        working_response = self._gradient(y, working_prediction)
        for idx in range(self.n_estimators):
            # Clone the weak_learner to create a new regression tree object.
            tree = clone(self.weak_learner)
            # Fit a regression tree to the working response.
            tree = tree.fit(X, working_response)
            # Compute the terminal node estimates for the fit regression tree.
            # The method _terminal_node_estimates should be used here.
            terminal_node_estimates = self._terminal_node_estimates(
                X, y, working_prediction, tree)
            # Compute the vector of updates of the current predictions.  The
            # method _prediction_update should be used here.
            prediction_update = self._prediction_update(
                X, tree, terminal_node_estimates)
            # Update the working_prediction using the results from
            # _prediction_update.  Don't forget to scale by the learning rate!
            working_prediction += self.learning_rate * prediction_update
            # Re-compute the working response (what we will fit the next tree
            # to).  Use the method _gradient to do this.
            working_response = self._gradient(y, working_prediction)
            self.estimators_.append(tree)
            self.terminal_node_estimates_.append(terminal_node_estimates)
        return self

    def predict(self, X):
        """Return predictions from a fit model.

        The log_predicted values are the sum of the baseline prediction with
        the predictions from all of the fit regression trees.  The final
        predicted values are the exponentials of the log_predicted values.

        Note that the predictions from regression trees used in gradient
        boosting are *not* the simple means of the target values in terminal
        nodes, instead we keep track of alternate terminal node predictions in
        the self.terminal_node_estimates_ attribute.

        Parameters
        ----------
        X: array, shape (n_samples, n_features)
            Data set.

        Returns
        -------
        prediction: array, shape (n_samples, )
            Array of predicted values of the samples in X.
        """
        log_prediction = np.repeat(self.initial_value_, X.shape[0])
        # Add the predictions from all the trees to the log_prediction.  You'll
        # need to loop through both the fit trees *and* the
        # terminal_node_estimates_.  Use the _prediction_update method to
        # compute the update to log_prediction.
        estimator_data = zip(self.estimators_, self.terminal_node_estimates_)
        for tree, tn_estimates in estimator_data:
            log_prediction += (
                self.learning_rate *
                self._prediction_update(X, tree, tn_estimates))
        return np.exp(log_prediction)
            
    def _initial_value(self, y):
        """Calculate the best constant prediction for the data y.

        In the case of Poisson boosting, the initial prediction is the
        logarithm of the mean of y.

        Parameters
        ----------
        y: array, shape (n_samples, )
            Target values.

        Returns
        -------
        initial_value: float
            The initial log_prediction before growing any trees.  Equal to the
            logarithm of the mean of y.
        """
        return np.log(np.mean(y))

    def _gradient(self, y, log_prediction):
        """Calculate the gradient of the loss function, evaluated at the data y
        and the current predictions.

        In Gradient Boosting, the regression trees are fit to the gradient of
        the loss function, evaluated at the current predicted values.  In this
        sense, the "gradient of the loss function" is the generalization of the
        residuals of the current predictions, as seen in Gradient Boosted
        Regression.

        In the case of Poisson boosting, the loss function is the Poisson
        log-likelihood, for which the gradient is y minus the prediction (just
        like in linear regression).

        Parameters
        ----------
        y: array, shape (n_samples, )
            Target values.

        log_prediction: array, shape (n_samples, )
            The logarithms of the current predicted values.

        Returns
        -------
        gradient: array, shape (n_samples, )
            The gradient of the Poisson likelihood, evaluated at the current
            predicted values.
        """
        return y - np.exp(log_prediction)

    def _terminal_node_estimates(self, X, y, log_prediction, tree):
        """Calculate the terminal node estimates from a fit regression tree.

        Parameters
        ----------
        X: array, shape (n_samples, n_features)
            Training data.

        y: array, shape (n_samples, )
            Target values.

        log_prediction: array, shape (n_sample, )
            The logarithms of the current predicted values, also equal to the
            sum of the estimated regression tree predictions.

        tree: sklean.tree object
            A fit regression tree.

        Returns
        -------
        terminal_node_estimates: dict(int: float)
            A dictionary whose keys are id's of terminal nodes in the tree (as
            returned from tree.apply), and whose values are the predictions
            associated to that node in the boosted model.

        This is the most subtle point in gradient boosting.  When we use
        regression trees in gradient boosting, we do *not* always use the mean
        of the target variable within a given terminal (leaf) node as the
        tree's predictions.  Instead, we calculate a custom prediction specific
        to the type of gradient boosting we are doing.

        In the case of Poisson boosting, we calculate the predictions in a
        terminal node as

                       sum of target in terminal node
           log( -------------------------------------------- )
                  sum of current predicted in terminal node  

        Note that the denominator here is the predicted value, *not* the
        logarithm of the predicted value.

        So this method needs to do the following:
          - Identify the terminal node in the tree associated with each row of X.
          - Calculate the quantity above for each terminal node in the tree.
          - Create a dictionary the associates each terminal node id with the
            prediction quantity above.
          - return this dictionary.
        """
        prediction = np.exp(log_prediction)
        estimates = {}
        terminal_node_assignments = tree.apply(X)
        terminal_node_idxs = np.unique(terminal_node_assignments)
        for idx in terminal_node_idxs:
            in_terminal_node = (terminal_node_assignments == idx)
            y_in_node = np.sum(y[in_terminal_node])
            if not y_in_node:
                y_in_node += 1e-300
            prediction_in_node = np.sum(prediction[in_terminal_node])
            if not prediction_in_node:
                prediction_in_node += 1e-300
            estimates[idx] = np.log(y_in_node / (prediction_in_node))
        return estimates

    def _prediction_update(self, X, tree, terminal_node_estimates):
        """Array of prediction updates to current log_predicted values:

            new_log_predicteds = current_log_predicteds + prediction_update

        Note that this method only calculates the prediction_update term of the
        above equation, it does not actually update an array of predictions.

        Parameters
        ----------
        X: array, shape (n_samples, n_features)
            Training data.

        tree: sklean.tree object
            A fit regression tree.

        terminal_node_estimates: dict(int: float)
            A dictionary whose keys are id's of terminal nodes in the tree (as
            used to index terminal nodes in tree.apply), and whose values are
            the predictions associated to that node in the boosted model.

        Returns
        -------
        prediction_update: array, shape (n_samples, )
            Updates to the current array of log_predicted values.
        """
        prediction_update = np.zeros(X.shape[0])
        terminal_node_assignments = tree.apply(X)
        for idx in terminal_node_estimates:
            in_terminal_node = (terminal_node_assignments == idx)
            prediction_update[in_terminal_node] = terminal_node_estimates[idx]     
        return prediction_update