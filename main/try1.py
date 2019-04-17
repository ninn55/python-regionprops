# -*- coding: utf-8 -*-  
""" 
 Created by ninn55 on 2018/5/8 14:48
 @contact: uestcnwx@gmail.com 
 @github profile: https://github.com/ninn55
 @software: PyCharm  @since:Anaconda 4.4.10 python 3.6.4
 """

from skimage.io import imread, imshow, imsave
from matplotlib import pyplot as plt
import numpy as np

def area(im):
    rd = [[1, 0], [1, -1], [1, 1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
    dic = np.argwhere(im == True)
    bak = dic
    a = {}
    #print(dic.shape, dic[0], im.shape)
    for i in range(len(1)):
        if dic[i, :] not in bak:
            continue
        else:
            temp = dic[i, :]
            a[len(a) + 1] = temp
            bak = bak[np.logical_not(np.all([bak[:, 0] == temp[0], bak[:, 1] == temp[1]], axis=0))]
            for i in range(8):
                pass




    return a

def jug_1(point, dic, bak):
    rd = [[1, 0], [1, -1], [1, 1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
    X = True
    for i in range(8):
        temp = point + rd[i, :]
        X = X & ((temp not in dic) | (temp not in bak))
    return X

def jug_2(point, dic, bak):
    temp_1 = point in dic
    temp_2 = point not in bak
    X = False
    if temp_1 and temp_2:
        X = True
    return X

if __name__ == '__main__':
    #print(getcwd())
    a = imread('../assets/circlesBrightDark.png')
    #print(a.dtype, a.shape)
    plt.figure()
    imshow(a[:, :, 1] < 100)
    plt.show()
    plt.figure()
    imshow(a)
    plt.show()
    im = (a[:, :, 1] < 100)
    #area(im)
