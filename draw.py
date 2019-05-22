# -*- coding: utf-8 -*-
# by opqnext.com, 2017.02.08

try:
    from PIL import Image
except Exception as e:
    print "[>] pip install pillow"
else:
    pass
finally:
    pass


import argparse
 
# 接收参数
parser = argparse.ArgumentParser()
 
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('-w','--width', type=int, default=80)
parser.add_argument('-hh','--height', type=int, default=80)
 
args = parser.parse_args()
 
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
 
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\"^`' ")
 
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
 
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]
 
if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    file = open(OUTPUT,"w+")
    file.write(txt)
    file.close()
 
    print txt
