# Automated-text-recognition

This project provides tools for extracting text and characters from images, videos, and live camera feeds using Python, OpenCV, and Tesseract OCR. It includes three main components:

1. **Image Character Extraction**: Extracts text from uploaded images and highlights the bounding boxes of detected text.
2. **Video Character Extraction**: Extracts text from videos, with bounding boxes around detected text.
3. **Live Camera Character Extraction**: Extracts text from live camera feeds, with bounding boxes around detected text.

## Prerequisites

Make sure you have the following installed:
- Python 3.x
- OpenCV (`cv2`)
- Pillow (`PIL`)
- Pytesseract
- Tkinter

Additionally, you must have Tesseract OCR installed on your machine. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Ajaneeshwar/Automated-text-recognition.git
    cd Automated-text-recognition
    ```

2. **Install Dependencies**:
    ```sh
    pip install opencv-python Pillow pytesseract matplotlib
    ```

3. **Configure Tesseract**:
    Update the `pytesseract.pytesseract.tesseract_cmd` path to the location where Tesseract OCR is installed on your machine. For example:
    ```python
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ```

## Usage

### 1. Image Character Extraction

To extract text from an image:
1. Run the `image_extraction.py` script:
    ```sh
    python image_extraction.py
    ```
2. Click the "Upload an image" button to select an image file.
3. Click the "Extract text" button to extract text and see the bounding boxes.

### 2. Video Character Extraction

To extract text from a video file:
1. Place your video file (`test.mp4`) in the project directory.
2. Run the `video_extraction.py` script:
    ```sh
    python video_extraction.py
    ```
3. The video will play, and detected text will be highlighted with bounding boxes. Press 'q' to quit the video.

### 3. Live Camera Character Extraction

To extract text from a live camera feed:
1. Run the `live_camera_extraction.py` script:
    ```sh
    python live_camera_extraction.py
    ```
2. The camera feed will display, and detected text will be highlighted with bounding boxes. Press 'q' to quit the feed.

## Scripts Overview

### `image_extraction.py`

```python
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root = Tk()
root.title('Text Extraction from Images')
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
newline = Label(root)
uploaded_img = Label(root)

def imgextract(path):
    img = cv2.imread(path)
    Sample_img = cv2.resize(img, (400, 350))
    img2char = pytesseract.image_to_string(img)
    imgH, imgW, _ = img.shape
    imgbox = pytesseract.image_to_boxes(img)
    for boxes in imgbox.splitlines():
        boxes = boxes.split(' ')
        x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
        cv2.rectangle(img, (x, imgH - y), (w, imgH - h), (255, 50, 0), 1)
    print("RESULT\n\n\n", img2char)
    return img2char, img, imgbox

def show_extract_button(path):
    extractBtn = Button(root, text="Extract text", command=lambda: imgextract(path), bg="#2f2f77", fg="white", pady=15, padx=15, font=('Times', 15, 'bold'))
    extractBtn.pack()

def upload():
    try:
        path = filedialog.askopenfilename()
        image = Image.open(path)
        img = ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image = img
        show_extract_button(path)
    except:
        pass

uploadbtn = Button(root, text="Upload an image", command=upload, bg="#2f2f77", fg="white", height=2, width=20, font=('Times', 15, 'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()
root.mainloop()
```

### `video_extraction.py`

```python
import pytesseract
import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture("test.mp4")

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open Video")

cntr = 0
while True:
    ret, frame = cap.read()
    cntr += 1
    if (cntr % 8) == 0:
        imgH, imgW, _ = frame.shape
        x1, y1, w1, h1 = 0, 0, imgH, imgW
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            cv2.rectangle(frame, (x, imgH - y), (w, imgH - h), (0, 0, 255), 3)
        cv2.putText(frame, imgchar, (x1 + int(w1 / 50), y1 + int(h1 / 50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
        cv2.imshow('Character Extraction from Video', frame)
    if cv2.waitKey(2) == ord('e'):
        print(imgchar)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### `live_camera_extraction.py`

```python
import pytesseract
import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open Camera")

cntr = 0
while True:
    ret, frame = cap.read()
    if (cntr % 2) == 0:
        imgH, imgW, _ = frame.shape
        x1, y1, w1, h1 = 0, 0, imgH, imgW
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            cv2.rectangle(frame, (x, imgH - y), (w, imgH - h), (0, 0, 255), 1)
        cv2.putText(frame, imgchar, (x1 + int(w1 / 50), y1 + int(h1 / 50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.imshow('Character Extraction from Live Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- [Python](https://www.python.org/)
