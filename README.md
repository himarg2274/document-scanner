# Document Scanner using OpenCV

This is a Python-based document scanner that detects a rectangular document in an image, extracts it by performing a perspective transform, and outputs a flattened, grayscale scanned version. The algorithm detects edges, finds contours, and warps the document to a top-down view.

---

## Features

- Reads an input image with a document or rectangular object  
- Detects the largest 4-point contour approximating the document boundary  
- Reorders points for correct perspective transformation  
- Applies perspective warp to obtain a flattened, front-facing document  
- Converts the scanned document to grayscale for easy reading or further processing  
- Visualizes all steps using `matplotlib`

---

## Example Input and Output

### Input Image
![paid-bill](https://github.com/user-attachments/assets/1e51b57a-4e06-4b10-bd64-adcad0d3f68e)


### Detected Contour
![Untitled](https://github.com/user-attachments/assets/63771a43-2c58-4f04-88ca-a76aa3865ff1)


### Warped Document (Output)
![Untitled](https://github.com/user-attachments/assets/522de5a6-2ddb-48ae-81e1-de18779f2743)


### Final Grayscale Result
![Untitled](https://github.com/user-attachments/assets/ac2b6acd-e289-4f7e-9b01-77dccffc2d02)



## Requirements

- Python 3.x  
- OpenCV (`cv2`)  
- NumPy (`numpy`)  
- Matplotlib (`matplotlib`)

Install dependencies with:

```bash
pip install opencv-python numpy matplotlib

