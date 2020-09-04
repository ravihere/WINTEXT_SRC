from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from PIL import Image
import pytesseract
import cv2
from .forms import reqData
def index(request):
	return render(request,'TE/index.html')
def wintext(request):
    return render(request, 'TE/WinText.html')
def about(request):
    return render(request, 'TE/About.html')
def get_text(request):
    # check to see if this is a post request
    if request.method == "POST":
        try:
            lang=request.POST['lang']    
        except:
            return render(request,'TE/WinText.html')
            # check to see if an image was uploaded
        if request.FILES.get("image", None) is not None:
            image = request.FILES["image"]
        try:
            image = cv2.imread(image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (3,3), 0)
            thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            # Morph open to remove noise and invert image
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
            invert = 255 - opening
            pytesseract.pytesseract.tesseract_cmd ='/app/.apt/usr/bin/tesseract'
            result = pytesseract.image_to_string(invert, lang=lang,config='--psm 6')
            result= result.replace('\n\n','\n')
            context={
            'result':result,
            }
        except:
            return render(request, 'TE/WinText.html')
    return render(request, 'TE/WinText.html', context)
