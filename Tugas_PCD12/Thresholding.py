import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import sobel

image = imageio.imread('C:\\Users\\Galang\\Documents\\TUGAS TUGAS KULIAH\\Tugas_PCD12\\Pmg.jpg')

gray_image = np.mean(image, axis=2)

sobel_x = sobel(gray_image, axis=0)
sobel_y = sobel(gray_image, axis=1)
edges = np.hypot(sobel_x, sobel_y)

threshold_value = 100
binary_output = edges > threshold_value

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Citra Deteksi Tepi')
plt.imshow(edges, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Hasil Segmentasi')
plt.imshow(binary_output, cmap='gray')
plt.show()