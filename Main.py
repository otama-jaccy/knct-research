#coding: utf-8

import ADMM
import Util
from PIL import Image
import sys
import Const
import numpy as np

if __name__ == '__main__':
    args = sys.argv
    file_name = args[1]
    img = Image.open(file_name)

    img_v = Util.imageToVec(img)
    admm = ADMM.ADMM(img_v, img.size[0], img.size[1])
    img_v = admm.calculate()
    img = Util.vecToImage(img_v[::-1], img.size)

    img.show()