# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/8 17:21'
import math
import numpy as np


def calLongestDistance(R, theta1, theta2):
    x = np.arange(0, 360)
    theta1 = (np.pi/180.0)*x
    theta2 = (np.pi/180.0)*x
    X1 = R*math.cos(theta1)
    Y1 = R*math.sin(theta1)
    X2 = R*math.cos(theta2)
    Y2 = R*math.sin(theta2)
    s = math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
    while True:
        for theta1 in range(0, 360):
            for theta2 in range(0, 360):
                if s == (theta1 - theta2):
                    print(float)
                    return s

if __name__ == '__main__':

    a = int(input("please dot nums", int, float))
    print(calLongestDistance())