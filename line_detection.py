def draw_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

# Detect lines using Hough Transform
lines = cv2.HoughLinesP(roi_image, rho=1, theta=np.pi/180, threshold=50, minLineLength=40, maxLineGap=5)
line_image = draw_lines(image, lines)

# Combine with original image
combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)

# Display the result
plt.figure(figsize=(12, 6))
plt.title("Lane Detection")
plt.imshow(combo_image)
plt.show()
