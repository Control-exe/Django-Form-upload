from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import os
from django.conf import settings
from .models import Conect
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "app/index.html")
    
def conect(request):    
    upload = Conect()
    upload.company = request.POST.get("company")
    upload.text = request.POST.get("text")
    
    #block image upload & save
    upload.image = request.FILES.get("image")
    img = Image.open(upload.image)
    path = os.path.join(settings.BASE_DIR, f"media/image/{upload.image.name}.jpg")

    upload.description_image = request.POST.get("description_image")
    
    #block xlsx upload & save
    upload.spreadsheet = request.FILES.get("spreadsheet")
    arq = pd.read_excel(upload.spreadsheet)
    path = os.path.join(settings.BASE_DIR, f"media/xlsx/{upload.spreadsheet.name}.xlsx")
    
    upload.save()

    return HttpResponse()

    #return HttpResponse(f"{options} {text} {image} {description_image} {file}")
        

"""def index(request):
    if request.method == "GET":
        return render(request, "app/src/index.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")

        mc = Conect(title="my_file", arq=file)
        mc.save()

        print(file)
        return HttpResponse('Enviado')"""