# Lane Detection Using Computer Vision and Edge Detection
pip install opencv-python numpy matplotlib tensorflow

## Description
This project implements a basic lane detection system for roads using computer vision techniques. It includes steps like edge detection, region of interest masking, and line detection to identify lane markings. This forms the basis for advanced autonomous driving applications.

## Features
- **Canny Edge Detection:** Extracts edges from the road image.
- **Region of Interest (ROI):** Focuses on the area of the image where lanes are most likely to be found.
- **Hough Transform:** Detects lane lines based on the edges identified.
- **Visualization:** Displays the detected lanes overlaid on the original road image.

## Technologies Used
- **Python**
  - OpenCV: For image processing.
  - NumPy: For mathematical operations.
  - Matplotlib: For visualization.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lane-detection.git
