from django.urls import path
from app3_1.views import *

urlpatterns = [
    path('index/', index),
    # path('migrate/', migrate),
    path('allpersons/', allpersons),
]