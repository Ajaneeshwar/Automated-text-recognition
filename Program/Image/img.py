#!/usr/bin/env python
# coding: utf-8

# # Extraction of Character from Images

# In[ ]:


from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract 
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root = Tk()
root.title('Text Extraction from Images')
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

newline= Label(root)
uploaded_img=Label(root)


def imgextract(path):
    img = cv2.imread(path)
    Sample_img = cv2.resize(img,(400,350))

    img2char = pytesseract.image_to_string(img)    
    imgH, imgW, _ = img.shape  
    imgbox = pytesseract.image_to_boxes(img)
    for boxes in imgbox.splitlines():
        boxes = boxes.split(' ')
        x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
        cv2.rectangle(img,(x,imgH-y),(w,imgH-h),(255,50,0),2)

    print("RESULT\n\n\n", img2char)
    #plt.imshow(img)
    #print("\n\n\n\n\nBounding Box\n\n",imgbox, "\n\n\n\nBounding Box Output")
    return img2char, img, imgbox

    


def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: imgextract(path),bg="#2f2f77",fg="white",pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.pack()

def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass  

uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="white",height=2,width=20,font=('Times',15,'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()


root.mainloop()

