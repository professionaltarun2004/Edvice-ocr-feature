from django.shortcuts import render
from .forms import ImageUploadForm
from googletrans import Translator
import pytesseract
from PIL import Image, ImageOps
import cv2
import numpy as np
from io import BytesIO

def preprocess_image(image):
    img = np.array(image)
    if len(img.shape) == 3: 
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    elif len(img.shape) == 2:  
        pass
    else:
        raise ValueError("Unsupported image format")
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img

translator = Translator()

def image_upload(request):
    text = ''
    translated_text = ''
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            img = Image.open(image_file)

            if img.mode != 'RGB':
                img = img.convert('RGB')

            img = preprocess_image(img)
            img = Image.fromarray(img)

            text = pytesseract.image_to_string(img)
            translated_text = translator.translate(text, dest='hi').text

    else:
        form = ImageUploadForm()

    return render(request, 'ocr_app/upload.html', {
        'form': form,
        'text': text,
        'translated_text': translated_text
    })

