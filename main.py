# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from imageio import imread,imwrite

# array in numpy, matrices


def show_me():
    # load image as pixel array
    my_pic = mpimg.imread("C:\\Users\\USER\\Desktop\\AMIT\\year4\\Image processing\\try37\\me.jpeg")
    plt.imshow(my_pic)
    plt.show()

# import pic


if __name__ == '__main__':
    my_im = imread('papilio_caterpillars.jpg')
    # returns num of rows, cols
    print(my_im.shape)
    # returns array size of 1X3 when the pic is RGB - the num of pixel in accordance with the color
    print(my_im[530,2000])

    # taking the biggest caterpillar and make a copy of it in different place over the picture
    caterpillar = my_im[500:1000,1700:2500]
    my_im[2000:2500,0:800] = caterpillar
    plt.imshow(my_im)
    plt.show()

    my_im_float = my_im.astype(np.float64)

    # Hi from Alon


