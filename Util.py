#coding: utf-8
#画像配列をrgbが並んだベクトルにする
def imageToVec(img):
    width = img.size[0]
    height = img.size[1]
    vec = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            vec.append(r)
            vec.append(g)
            vec.append(b)
    return vec

def vecToImage(vec, size):
    from PIL import Image
    img = Image.new('RGBA', size)
    width = size[0]
    height = size[1]
    for y in range(height):
        for x in range(width):
            idx = y*width*3+x*3
            #r,g,b = vec[idx:idx+3]
            r = vec[idx]
            g = vec[idx+1]
            b = vec[idx+2]
            img.putpixel((x, y), (r, g, b, 0))
    return img