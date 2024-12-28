def region_of_interest(image):
    height, width = image.shape
    mask = np.zeros_like(image)

    # Define a triangular region of interest
    polygon = np.array([
        [(0, height), (width, height), (width // 2, height // 2)]
    ])
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

# Apply ROI mask
roi_image = region_of_interest(edges)

# Display the ROI image
plt.figure(figsize=(6, 6))
plt.title("Region of Interest")
plt.imshow(roi_image, cmap="gray")
plt.show()
