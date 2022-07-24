
from django.urls import path
from epanel.views import index, new

# CRUD App using Models
# User Management System
urlpatterns = [
    path('', index),
    path('new', new),
]
