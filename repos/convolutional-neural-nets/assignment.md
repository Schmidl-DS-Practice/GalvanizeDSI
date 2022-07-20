# Convolutional Neural Networks

## Basic

### Part 1: MNIST Classification
You will be revisiting the MNIST digits but with a more formidable 
image classification tool:  a convolutional neural net.  Take the pre-existing code
in `src/cnn.py` and tune it to improve performance. You should be able to get 
above 98% accuracy. 

## Advanced

### Part 2: Cats and Dogs
Cat and dog images are located in the `data` directory.  These images are a subset 
of data available from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data).  
Follow this [Keras blog post](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html) 
to create an effective CNN Cat/Dog Classifier on the little data you have in only 
40 lines of code.  This blog post was written in June 2016 when Keras was separate 
from Tensorflow.  As of October 2019, Keras is part of Tensorflow and the way
you use it (the API) has changed.  See [here](https://www.pyimagesearch.com/2019/10/21/keras-vs-tf-keras-whats-the-difference-in-tensorflow-2-0/)
for more information.  The point is that the code in the blog post will need to
be modified to use the `tf.keras` API.  [Here](https://www.tensorflow.org/tutorials/keras/classification) 
is documentation of the new syntax.  

Take note of the pipeline used to process (augment) the images before fitting.

DO NOT copy-and-paste any of the code but instead retype anything you use, 
experimenting along the way by tweaking the parameters and the number of nodes.
