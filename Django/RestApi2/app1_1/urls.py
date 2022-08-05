from django.urls import path
from . import views

urlpatterns = [
    path('v1', views.HelloView.as_view(), name='hello'),
]