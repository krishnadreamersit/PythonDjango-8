from django.urls import path
from app1_6.views import *

urlpatterns = [
    path('index/', index),
]