import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a sample road image
image = cv2.imread("road_sample.jpg") 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Display the original and grayscale images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Grayscale Image")
plt.imshow(gray_image, cmap="gray")
plt.show()
