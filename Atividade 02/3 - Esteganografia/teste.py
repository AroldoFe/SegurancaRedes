from PIL import Image
import numpy as np

w, h = 3, 2
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0, 0] = [255, 0, 0]
data[0, 1] = [0, 255, 0]
data[0, 2] = [0, 0, 255]
data[1, 0] = [255, 0, 0]
data[1, 1] = [0, 255, 0]
data[1, 2] = [0, 0, 255]
img = Image.fromarray(data, 'RGB')
img.save('my.bmp')
img.show()