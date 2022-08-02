from django.urls import path
from . import views # 1

urlpatterns = [
    path('send_value1', views.receive_value1),
    path('send_value2/<full_name>', views.receive_value2),

    path('display_form1', views.display_form1),
    path('get_form1', views.get_form1),

    path('display_form2', views.display_form2),
    path('get_form2', views.get_form2),

    path('display_form3', views.display_form3),
    path('get_form3', views.get_form3),
]