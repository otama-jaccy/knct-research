#coding:utf-8

import numpy as np

class VariableCreater:
    def createD(self, width, height):
        N = width*height
        ROW = 3*N
        COLUMN = 6*N
        array = [[0 for x in range(ROW)] for y in range(COLUMN)]
        for row in range(COLUMN):
            x1 = int(row/2)
            dx = width*3 if row%2==0 else 3
            x2 = x1+dx
            x2 = x2 if x2<ROW else x1-dx
            array[row][x1] = 1
            array[row][x2] = -1
        return np.matrix(array, dtype=np.int8)

if __name__ == '__main__':
    from numpy import linalg as la
    from PIL import Image
    import sys
    im = Image.open("line.png")
    rgb_im = im.convert('RGB')
    size = rgb_im.size

    nega_im = Image.new('RGBA', size)
    u = []
    for y in range(size[1]):
        for x in range(size[0]):
            r, g, b = rgb_im.getpixel((x, y))
            u.append(r)
            u.append(g)
            u.append(b)
    creater = VariableCreater()
    D = creater.createD(size[0],size[1])

    u = np.matrix(u)
    print(len(u))
    im = np.dot(D,u.T)
    width = size[0]
    height = size[1]
    nega_im = Image.new('RGBA', size)
    for y in range(height):
        for x in range(width):
            idx = y*width*6+x*6
            r = im[idx] + im[idx+1]
            g = im[idx+2] + im[idx+3]
            b = im[idx+4] + im[idx+5]
            r = int(abs(r))
            g = int(abs(g))
            b = int(abs(b))
            nega_im.putpixel((x, y), (r, g, b, 0))
    nega_im.show()