from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize
import os
import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.feature import canny

def open_images(path):
    
    train_images = imread(path)
    gray_image = rgb2gray(train_images) #for making image gray scale    
    gray_size = resize(gray_image, (300, 300))
    # size_me = resize(train_images, (300,300))
    return gray_size.sobel()

if __name__ == '__main__':
   
    # beach = imread('data/beach.jpg')
    # forest = imread('data/forest.jpg')
    # male = imread('data/male.jpg')
    # female = imread('data/female.jpg')
    # path = [beach, forest, male, female]
    
    # fig, axes = plt.subplots()
    # axes.imshow(beach)
    # plt.show()
    open = open_images('data/beach.jpg')
    print(open)

