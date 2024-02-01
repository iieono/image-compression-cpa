import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

image = cv2.cvtColor(cv2.imread('img1.png'), cv2.COLOR_BGR2RGB )

print(image.shape)

plt.imshow(image)

r, g, b = cv2.split(image)

rgb = r / 255, g / 55, b / 255