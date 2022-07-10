from django.urls import path
from site1.views import index

urlpatterns = [
    path('', index),
]