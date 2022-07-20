'''
Code implements multi-perceptron neural network to classify MNIST images of
handwritten digits using Keras and Tensorflow.  Based on code from
https://www.packtpub.com/books/content/training-neural-networks-efficiently-using-keras

'''

import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from tensorflow.keras.metrics import Precision, Recall

def load_and_condition_MNIST_data():
    ''' loads and shapes MNIST image data '''
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    print("\nLoaded MNIST images")
    X_train = X_train.astype(np.float32) #before conversion were uint8
    X_test = X_test.astype(np.float32)
    X_train.resize(len(y_train), 784) # 28 pix x 28 pix = 784 pixels
    X_test.resize(len(y_test), 784)
    #print('\nFirst 5 labels of MNIST y_train: {}'.format(y_train[:5]))
    y_train_ohe = to_categorical(y_train) # one hot encode the target
    #print('\nFirst 5 labels of MNIST y_train (one-hot):\n{}'.format(y_train_ohe[:5]))
    #print()
    return X_train, y_train, X_test, y_test, y_train_ohe

def sigma(x):
    return 1 / (1 + 1 / np.exp(x))


if __name__ == '__main__':
    X_train, y_train, X_test, y_test, y_train_onehot = load_and_condition_MNIST_data()
    #print(X_train.shape)
    #print(X_test.shape)
    
    #fig, ax = plt.subplots()
    #ax.imshow(X_train[0].reshape(28,28))

    # clf = DecisionTreeClassifier()
    # clf.fit(X_train, y_train)
    # yhat = clf.predict(X_test)
    # print(accuracy_score(y_test, yhat))

    np.random.seed(42)
    n_samples, n_feats = X_train.shape
    #print(n_samples, n_feats, X_test.shape)

    model = Sequential() # sequence of layers

    denselayer = Dense(units=1,
                    input_dim=n_feats,
                    kernel_initializer='uniform',
                    activation='sigmoid')

    model.add(denselayer)

    #plt.hist(model.predict(X_test))
    #plt.show()

    #model.predict(X_test).shape
    #model.get_layer(index=0).activation
    model.get_layer(index=0).activation(X_train[0] @ model.get_weights()[0])
    sig = sigma(X_train[0] @ model.get_weights()[0])
    #print(sig)

    y_train==1
    yone_train = y_train==1
    yone_test = y_test==1
    model.compile(loss='binary_crossentropy', optimizer="sgd",
                    metrics=[Precision(), Recall()] ) 

    model.fit(X_train, yone_train, epochs=10, batch_size=5000, verbose=1,
                validation_split=0.1)