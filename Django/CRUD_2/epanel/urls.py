
from django.urls import path
from epanel.views import index, new, edit, delete

# CRUD App using Models
# User Management System
urlpatterns = [
    path('', index),
    path('new', new),
    path('edit', edit),
    path('delete', delete),
]
