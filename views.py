from django.shortcuts import render
import cv2
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import numpy as np
from django.core.files.base import ContentFile

# Create your views here.

from django.shortcuts import render

def camera_view(request):
    return render(request, 'image_gallery.html')
