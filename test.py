#coding: utf-8

from PIL import Image
import sys

args = sys.argv
file_name = args[1]
im = Image.open(file_name)

rgb_im = im.convert('RGB')
size = rgb_im.size

nega_im = Image.new('RGBA', size)

for x in range(size[0]):
    for y in range(size[1]):
        r,g,b = rgb_im.getpixel((x,y))
        g = int((r +g + b)/3)
        nega_im.putpixel((x,y),(g,g,g,0))

nega_im.show()