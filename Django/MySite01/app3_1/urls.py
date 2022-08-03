from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index), # default
    path('get_value', views.get_value),
]
