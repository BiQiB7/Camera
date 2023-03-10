from django.urls import path
from . import views

urlpatterns = [
    # path('', views.capture_image, name = 'webcam'),
    path('', views.camera_view, name='camera'),
]