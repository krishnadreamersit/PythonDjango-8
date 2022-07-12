from django.urls import path
from app2_1.views import *

urlpatterns = [
    path('index/', index),
    path('getValues1', getValues1),
    path('getValues2', getValues2),
    path('getValues3', getValues3),
    path('getValues4/<int:pid>', getValues4), # localhost:8000/getValues4/1
]