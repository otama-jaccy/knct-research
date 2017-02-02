#coding: utf-8

import numpy as np

#Dを左からかける
def dotD(vec, width, height):
    ret = []
    for x1 in range(len(vec)):
        for dx in [3,width*3]:
            x2 = x1 + dx
            x2 = x2 if x2<len(vec) else x2-dx
            ret.append(vec[x1]-vec[x2])
    return ret

#Dの転置を左からかける
def dotDT(vec, width, height):
    N = width*height
    ret = [0 for i in range(3*N)]
    for x in range(3*N):
        idx = x*2
        ret[x] = vec[idx] + vec[idx+1]

    cou = 1
    for idx in range(3,3*N):
        ret[idx] -= vec[cou]
        cou+=2

    cou = 0
    for idx in range(3*width, 3*N):
        ret[idx] -= vec[cou]
        cou+=2
    return ret

#dotDのテストコード、エッジっぽいのが取れる
if __name__ == '__main__':
    from numpy import linalg as la
    from PIL import Image
    import sys
    im = Image.open("chigi")
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

    width = size[0]
    height = size[1]
    w = Calculator().dotD(u, width, height)
    im = Image.new('RGBA', size)

    for y in range(height):
        for x in range(width):
            idx = y*width*6+x*6
            r = w[idx] + w[idx+1]
            g = w[idx+2] + w[idx+3]
            b = w[idx+4] + w[idx+5]
            r = int(abs(r))
            g = int(abs(g))
            b = int(abs(b))
            im.putpixel((x, y), (r, g, b, 0))

    im.show()