from django.urls import path
from app1_4.views import index

urlpatterns = [
    path('index/', index),
]