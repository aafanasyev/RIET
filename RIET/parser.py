import os
import sys
import rawpy
from PIL import Image
import numpy as np
from scipy import misc

raw_file="img/WP_20131021_14_55_29_Pro.dng"
#raw_file="img/WP_20161203_11_12_20_Pro.jpg"

raw = rawpy.imread(raw_file)
row = 2000
column = 5000
print(rawpy.libraw_version)
print ("Bayer pattern:\n",raw.raw_pattern)
print ("Indices 0,1,2,3: ",raw.color_desc)
print ("Sizes of the image:",raw.sizes)
print ("Height of the image:",raw.sizes[0],"\nWidth of the image:",raw.sizes[1])
print ("Color at row:" + str(row) +",colomn:" + str(column) + ":", raw.raw_color(row, column))
print ("Bayer filter value at row:" + str(row) +",colomn:" + str(column) + ":", raw.raw_value(row, column))
#rgb = raw.postprocess()
#raw_colors = raw.raw_colors_visible
#raw_color = raw_colors[200, 200]+"\n"+ raw_colors[201, 200]+"\n"+raw_colors[201, 201]+"\n"+raw_colors[200, 201]
#print (raw.color_matrix)
#print (raw.color_matrix)
#print (raw_color)
#img = Image.fromarray(rgb) # Pillow image
#img.show()

#Get all green filtered pixels
#Detect indeces
#Get coordinates of all green pixels