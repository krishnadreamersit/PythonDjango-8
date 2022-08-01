from django.urls import path
from app1.views import *

urlpatterns = [
    path('', home), # display all
    path('form1', index), # display form
]
