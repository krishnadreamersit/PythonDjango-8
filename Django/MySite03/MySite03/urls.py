"""MySite03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app1_1.views import index # step-1
from app1_2.views import index as home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index), # step-2
    path('home/', home),
    path('app1_3/', include('app1_3.urls')),
    path('app1_4/', include('app1_4.urls')),
    path('app1_5/', include('app1_5.urls')),
]
