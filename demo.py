# adds image processing capabilities 
from PIL import Image
import pytesseract
 # opening an image from the source path
img = Image.open(a)      
  
# describes image format in the output 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'   
# converts the image to result and saves it into result variable 
result = pytesseract.image_to_string(img)
print(result)
