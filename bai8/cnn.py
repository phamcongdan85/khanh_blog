import numpy as np
import matplotlib.pyplot as plt
import cv2
import urllib.request
from io import BytesIO


url = str('https://imgur.com/nmGz7Lv.png')
with urllib.request.urlopen(url) as url:
    f = BytesIO(url.read())

X = np.array(Image.open(f))
print('Image shape: %s')