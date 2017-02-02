#codign: utf-8

import Calculator
import numpy as np
import Const

class ADMM:
    def __init__(self,img_v, width, height):
        self._u = img_v[:]
        self.u = img_v[:]
        self.width = width
        self.height = height
        self.v = Calculator.dotD(img_v, width, height)
        self.w = self.v[:]
        self.gamma = Const.gamma

    def updateU(self):
        sub = [self.v[i]-self.w[i] for i in range(len(self.v))]
        d = Calculator.dotDT(sub, self.width, self.height)
        d = [x/self.gamma for x in d]
        d = [self._u[i] + d[i] for i in range(len(self._u))]
        d = np.fft.fft2(np.matrix(d))
        f = np.fft.rfft(np.diag([x for x in range(6*self.width*self.height)]))
        u = list(np.dot(d,f))
        self.u = [x for x in u]


    def updateV(self):
        d = Calculator.dotD(self.u, self.width, self.height)
        d = [d[i] - self.w[i] for i in range(len(d))]
        l1 = np.sum([np.abs(x) for x in d])
        if l1>Const.alpha:
            d.sort(reverse=True)
            i = Const.alpha
            while i < len(d):
                d[i]=0
                i+=1
        self.v = d[:]


    def updateW(self):
        u = Calculator.dotD(self.u, self.width, self.height)
        self.w = [self.w[i] + u[i] - self.v[i] for i in range(len(u))]

    def calculate(self):
        n = 0
        while n < 20:
            self.updateU()
            self.updateV()
            self.updateW()
            self.gamma *= 0.8
            n += 1
            print(n)
        return self.u