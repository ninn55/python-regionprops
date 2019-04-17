# -*- coding: utf-8 -*-
"""
 Created by ninn55 on 2018/5/19 18:13
 @contact: uestcnwx@gmail.com
 @github profile: https://github.com/ninn55
 @software: PyCharm  @since:Anaconda 4.4.10 python 3.6.4
 """

import cv2
import os
import numpy as np

def show(im):
    if im.dtype == 'bool':
        im = im * 255
    im = im.astype('uint8')
    cv2.namedWindow('Image')
    cv2.imshow('Image', im)
    cv2.waitKey(0)

class Point(object):
    def __init__(self):
        self.up = []
        self.down = []
        self.nt = np.array([])
        self.layer = 0
        self.status = False
        self.loc = np.zeros(2)

def area(im):
    if im.dtype != 'bool':
        _, im = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)

    def check_status(A, loc, im):
        rd_8 = np.array([[1, 0], [1, -1], [1, 1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]])
        sd = loc + rd_8

        def check_point(A, point, im):
            temp1 = False
            for i in range(len(A)):
                temp1 = (A[i].loc == point).all()
                if temp1 == True:
                    break
            temp2 = im[point[0], point[1]] == False
            return temp1 or temp2

        temp = True
        for i in range(8):
            temp = temp and check_point(A, sd[i, :], im)

        return temp


    dic = np.argwhere(im == True)
    loc = dic[np.random.randint(0, len(dic)), :]
    while 1:
        A = []
        A.append(Point())
        A[0].loc = loc
        A[0].status = check_status(A, A[0].loc, im)
        break

    return A

if __name__ == '__main__':
    if os.getcwd().endswith('main'):
        a = cv2.imread('../assets/circlesBrightDark.png')
    else:
        a = cv2.imread('/assets/circlesBrightDark.png')
    #show((a[:, :, 0] < 100) * 255)
    im = a[:, :, 0] < 50
    #show(im)
    print(area(im))