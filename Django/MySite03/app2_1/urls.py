from django.urls import path
from app2_1.views import *

urlpatterns = [
    path('index/', index),
    path('getValues1', getValues1),
]