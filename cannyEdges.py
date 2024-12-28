# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv2.Canny(blurred_image, 50, 150)

# Display the edges
plt.figure(figsize=(6, 6))
plt.title("Canny Edges")
plt.imshow(edges, cmap="gray")
plt.show()
