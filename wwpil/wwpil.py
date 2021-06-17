#!/usr/bin/env python

import sys
import itertools

from PIL import Image
from random import randint

img_file_name = sys.argv[1]
effect = int(sys.argv[2])

img = Image.open(img_file_name)
pixels = img.load()
width, height = img.size

output_img = Image.new('RGB', (width*6, height))

if effect == 1:
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            for i, n in enumerate(range(255, 0, -50)):
                div = 255/n
                output_img.putpixel(
                    (x+width*i, y),
                    (randint(r//div, r), randint(g//div, g), randint(b//div, b))
                )

if effect == 2:
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            p = {'r':r, 'g':g, 'b':b}
            for i, perm in enumerate(itertools.permutations('rgb')):
                xr, xg, xb = perm
                output_img.putpixel((x+width*i, y), (p[xr], p[xg], p[xb]))

if effect == 3:
    pixel_list = list(img.getdata())

    for n, pixel in reversed(list(enumerate(pixel_list[::-1]))):
        output_img.putpixel((n%width+width*2, n//width), pixel)

    for y in range(height):
        row = pixel_list[y*width:y*width+width]

        for x, pixel in enumerate(row):
            output_img.putpixel((x, y), pixel)
        for x, pixel in enumerate(row[::-1]):
            output_img.putpixel((x+width, y), pixel)

        x = 0
        for li in (row[:width//2], row[width//2:]):
            for pixel in li[::-1]:
                output_img.putpixel((x+width*3, y), pixel)
                x += 1
        x = 0
        for li in (row[:width//2], row[::-1][width//2:]):
            for pixel in li:
                output_img.putpixel((x+width*4, y), pixel)
                x += 1
        x = 0
        for li in (row[width//2:][::-1], row[width//2:]):
            for pixel in li:
                output_img.putpixel((x+width*5, y), pixel)
                x += 1

output_img.save(f'output{effect}.png')
