from django.urls import path
from app4_1.views import *

urlpatterns = [
    path('', index),
    path('add/', add),
    path('display1/', display1),
    path('display2/', display2),
    path('update/', update),
    path('delete/', delete),
]