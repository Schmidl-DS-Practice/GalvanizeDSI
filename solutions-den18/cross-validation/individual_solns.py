#Part 1
#1
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn import model_selection, linear_model
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import pandas as pd

#2-3
boston = load_boston()
X = boston.data # Attribute data
y = boston.target # Housing prices
colNames = boston.feature_names # Feature names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


#Part 2

#2
def rmse(theta, thetahat):
	''' Compute Root-mean-squared-error '''
	return np.sqrt(np.mean((theta - thetahat) ** 2))

#3-4
def calc_linear():
	# Fit your model using the training set
	linear = LinearRegression()
	linear.fit(X_train, y_train)

	# Call predict to get the predicted values for training and test set
	train_predicted = linear.predict(X_train)
	test_predicted = linear.predict(X_test)

	# Calculate RMSE for training and test set
	trainErr = rmse(y_train, train_predicted)
	valErr = rmse(y_test, test_predicted)

	return (trainErr, valErr)


#5
'''
When we evaluate our RMSE on a new set of data, we gain an understanding of how well we are 
capturing the signal in our data.  We can build more complex models that may bend to perfectly
fit our training data.  However, these models are not going to extend well to a new set of data,
because they are likely overfit to our training data.  

By evaluating our performance metric on a new set of data, we assure that we are modeling signal
and not the noise in our data.
'''

#Part 3
def k_fold_linear():
	''' Returns error for k-fold cross validation. '''
	err_linear, index, num_folds = 0, 0, 5
	kf = KFold(n_splits= num_folds)
	error = np.empty(num_folds)
	linear = LinearRegression()
	for train, test in kf.split(X_train):
		linear.fit(X_train[train], y_train[train])
		pred = linear.predict(X_train[test])
		error[index] = rmse(pred, y_train[test])
		index += 1

	return np.mean(error)


def plot_learning_curve(estimator, label=None):
	''' Plot learning curve with varying training sizes'''
	scores = list()
	train_sizes = np.linspace(10,100,10).astype(int)
	for train_size in train_sizes:
		cv_shuffle = model_selection.ShuffleSplit(train_size=train_size, 
						test_size=200, random_state=0)
		test_error = model_selection.cross_val_score(estimator, X, y, cv=cv_shuffle)
		scores.append(test_error)

	plt.plot(train_sizes, np.mean(scores, axis=1), label=label or estimator.__class__.__name__)
	plt.ylim(0,1)
	plt.title('Learning Curve')
	plt.ylabel('Explained variance on test set (R^2)')
	plt.xlabel('Training test size')
	plt.legend(loc='best')
	plt.show()


def plot_errors():
	''' Plot errors from test and training sets '''
	m = X.shape[1]
	err_test, err_train = [], []
	linear = LinearRegression()
	for ind in range(m):
		linear.fit(X_train[:,:(ind+1)], y_train)

		train_pred = linear.predict(X_train[:,:(ind + 1)])
		test_pred = linear.predict(X_test[:,:(ind + 1)])

		err_test.append(rmse(test_pred, y_test))
		err_train.append(rmse(train_pred, y_train))

	x = range(1, m+1)
	plt.figure()
	plt.plot(x, err_test, label='Test error')
	plt.plot(x, err_train, label='Training error')
	plt.title('Errors')
	plt.ylabel('RMSE')
	plt.xlabel('Features')
	plt.legend()
	plt.show()


#Part 4
def adj_r2(X, predictors, r2):
	sampleSize = len(X)
	num = (1-r2)*(sampleSize - 1)
	den = sampleSize - predictors - 1
	return 1 - (num/den)

def rfe():
	score = np.zeros(len(colNames)+1)
	for i in range(1, len(colNames)+1):
		est = LinearRegression()
		selector = RFE(est, i).fit(X_train, y_train)
		score[i] = adj_r2(X_train, i, selector.score(X_test, y_test))
	plt.figure()
	plt.plot(np.arange(1, len(score)+1), score)
	plt.title('Adjusted R^2 vs. Feature Count')
	plt.xlabel('Number of features')
	plt.ylabel('Adjusted R^2')
	plt.legend()
	plt.show()


class forward_select(object):
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.best_score = 0.
        self.column_names = []
        self.keep = []
        self.X_orig = None
        self.X = None
        self.y = None

    def fit_transform(self, df, target):
        self.y = target
        self.column_names = df.columns.tolist()
        self.X_orig = df.values
        self.X = np.ones([self.X_orig.shape[0],1])
        
        while self.X_orig.shape[1] > 0:
            scores = []
            for feature in range(self.X_orig.shape[1]):
                X_temp = np.concatenate((self.X, self.X_orig[:, feature, None]), axis=1)
                scores.append(sm.OLS(self.y, X_temp).fit().rsquared_adj)
            best_idx = np.argmax(np.asanyarray(scores))

            if scores[best_idx] <= self.best_score:
                if self.verbose: 
                	print('Removed columns ->', self.column_names)
                	print('-> All done!')
                return self.X[:,1:]
            else:
                self.X = np.concatenate((self.X, self.X_orig[:, best_idx, None]), axis=1)
                self.X_orig = np.delete(self.X_orig, best_idx, axis=1)
                self.keep.append(self.column_names.pop(best_idx))
                self.best_score = scores[best_idx]
                if self.verbose: print('Kept \'%s\' for a best score of %s' % (self.keep[-1], self.best_score))

def gen_forward():
	df = pd.DataFrame(X, columns=colNames)
	forward = forward_select(verbose=True)
	forward.fit_transform(df, y)

def main():
	print('--- Part 2 ---')
	print('One-fold Cross Validation')
	print('(Training error, Validation error) = ', calc_linear())

	print('--- Part 3 ---')
	print('K-fold Cross Validation')
	print('K-fold error:', k_fold_linear())
	estimator = LinearRegression()
	plot_learning_curve(estimator, label='LinearRegression')
	plot_errors()

	print('--- Part 4 ---')
	rfe()
	gen_forward()

if __name__ == '__main__':
    main()
    
