import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("./bill.jpg")
original = image.copy()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edged = cv2.Canny(blurred, 75, 200)

# Find contours
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area and keep the largest ones
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

target = None

# Loop over contours to find a 4-point contour
for c in cnts:
    approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
    if len(approx) == 4:
        target = approx
        break

# Show detected contour
if target is not None:
    cv2.drawContours(image, [target], -1, (0, 255, 0), 3)
    plt.title("Detected Contour")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
    print("Original 4 points:", target.reshape(4, 2))
    print("*****")
else:
    print("No 4-point contour detected!")

# Reorder the 4 points if found
def reorder(points):
    # Reorder to [top-left, top-right, bottom-right, bottom-left]
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 2), dtype=np.float32)

    add = points.sum(1)
    diff = np.diff(points, axis=1)

    new_points[0] = points[np.argmin(add)]  # top-left
    new_points[2] = points[np.argmax(add)]  # bottom-right
    new_points[1] = points[np.argmin(diff)] # top-right
    new_points[3] = points[np.argmax(diff)] # bottom-left
    return new_points

# Proceed only if target was found and valid
if target is not None and target.shape[0] == 4:
    target = reorder(target)
    print("Reordered points:", target)

    # Define destination points for perspective transform
    width = int(max(np.linalg.norm(target[0] - target[1]), np.linalg.norm(target[2] - target[3])))
    height = int(max(np.linalg.norm(target[0] - target[3]), np.linalg.norm(target[1] - target[2])))

    dst = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype="float32")

    # Perspective transform
    M = cv2.getPerspectiveTransform(target, dst)
    print("Perspective matrix:\n", M)

    ans = cv2.warpPerspective(original, M, (width, height))

    # Show warped image
    plt.title("Warped Document")
    plt.imshow(cv2.cvtColor(ans, cv2.COLOR_BGR2RGB))
    plt.show()

    # Convert to grayscale
    ans_gray = cv2.cvtColor(ans, cv2.COLOR_BGR2GRAY)
    plt.title("Final Grayscale Result")
    plt.imshow(ans_gray, cmap='gray')
    plt.show()
else:
    print("Invalid or no contour to warp.")
