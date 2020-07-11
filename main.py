import cv2
import pytesseract
import time
from openpyxl import Workbook
import translate

imgpath = 'test.png'
split_data = imgpath.split('.')
file_name = split_data[0]
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
text = pytesseract.image_to_string(img)
print("Before :\n",text)

ko = translate.trl(text)
print("After :\n",ko)

f=open(file_name+".txt", "w")
f.write(ko)
f.close()

