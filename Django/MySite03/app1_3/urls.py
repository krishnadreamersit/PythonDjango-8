from django.urls import path
from app1_3.views import index

urlpatterns = [
    path('index/', index),
]