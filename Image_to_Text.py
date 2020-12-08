import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Administrator\AppData\Local\Tesseract-OCR\tesseract.exe' # location where you have installed the tesseract OCR application 
from PIL import Image

img_name= input("Enter image file's name with extension: ")
file_name= input("Enter name of file which you would like to create : ")
file_name= file_name+".txt"
img = Image.open(img_name)
text = tess.image_to_string(img)

print(text)
file1 = open(file_name,"a+")
file1.writelines(text)
file1.close() #to change file access modes  
file1= open("myfile.txt","r+")